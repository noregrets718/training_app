from ast import Dict, List
from datetime import date
from fastapi import APIRouter, Request, Query, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.session_maker_fast_api import db
from app.api.dao import UserDAO, WorkoutDAO, ExerciseDAO
from loguru import logger
from app.api.schemas import TelegramIDModel,WorkoutFromClient, WorkoutCreateUserModel, WorkoutReadModel


router = APIRouter()



@router.get("/users/{telegram_id}/workouts")
async def get_user_workouts(
    telegram_id: int,
    session: AsyncSession = Depends(db.get_db)
):
    logger.info("обращение к эндпоинту workouts")
    user = await UserDAO.find_one_or_none(session=session, filters=TelegramIDModel(telegram_id=telegram_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    workouts = await WorkoutDAO.get_by_user_id(session=session, user_id=user.id)
    return workouts


@router.post("/workouts")
async def create_user_workout(
    workout: WorkoutFromClient,
    session: AsyncSession = Depends(db.get_db_with_commit)
):
    user_id = await UserDAO.get_user_id_by_tg_id(session=session, telegram_id=workout.telegram_id)
    if not user_id:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    values = WorkoutCreateUserModel(
        user_id=user_id,
        workout_date=workout.workout_date,
        exercises=workout.exercises
    )

    new_workout = await WorkoutDAO.add_full_workout(session=session, workout_data=values)
    return {"status": "ok", "workout_id": new_workout.id}



@router.get("/workouts/{workout_id}")
async def get_workout(workout_id: int, session: AsyncSession = Depends(db.get_db)):
    workout = await WorkoutDAO.get_full_by_id(session, workout_id)
    if not workout:
        raise HTTPException(404, detail="Тренировка не найдена")
    return WorkoutReadModel.model_validate(workout)



@router.get("/exercises")
async def get_exercises(
    session: AsyncSession = Depends(db.get_db)
):
    exercises = await ExerciseDAO.find_all(session=session)
    if not exercises:
        raise HTTPException(status_code=404, detail="User not found")
    return exercises