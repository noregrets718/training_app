# from fastapi import APIRouter, Depends, HTTPException
# from loguru import logger
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.dao.session_maker_fast_api import db
# from app.users.dao import UserDAO
# from app.users.schemas import TelegramIDModel
# from app.workouts.dao import WorkoutDAO
# from app.workouts.schemas import WorkoutFromClient, WorkoutCreateUserModel, WorkoutReadModel




# router = APIRouter()

# @router.get("/users/{telegram_id}/workouts")
# async def get_user_workouts(
#     telegram_id: int,
#     session: AsyncSession = Depends(db.get_db)
# ):
#     logger.info("обращение к эндпоинту workouts")
#     user = await UserDAO.find_one_or_none(session=session, filters=TelegramIDModel(telegram_id=telegram_id))
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     workouts = await WorkoutDAO.get_by_user_id(session=session, user_id=user.id)
#     return workouts


# @router.post("/workouts")
# async def create_user_workout(
#     workout: WorkoutFromClient,
#     session: AsyncSession = Depends(db.get_db_with_commit)
# ):
#     user_id = await UserDAO.get_user_id_by_tg_id(session=session, telegram_id=workout.telegram_id)
#     if not user_id:
#         raise HTTPException(status_code=404, detail="Пользователь не найден")

#     values = WorkoutCreateUserModel(
#         user_id=user_id,
#         workout_date=workout.workout_date,
#         exercises=workout.exercises
#     )

#     new_workout = await WorkoutDAO.add_full_workout(session=session, workout_data=values)
#     return {"status": "ok", "workout_id": new_workout.id}



# @router.get("/workouts/{workout_id}")
# async def get_workout(workout_id: int, session: AsyncSession = Depends(db.get_db)):
#     workout = await WorkoutDAO.get_full_by_id(session, workout_id)
#     if not workout:
#         raise HTTPException(404, detail="Тренировка не найдена")
#     return WorkoutReadModel.model_validate(workout)






from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
from typing import List

from app.dao.session_maker_fast_api import db
from app.users.dao import UserDAO
from app.users.schemas import TelegramIDModel
from app.workouts.dao import WorkoutDAO
from app.workouts.schemas import WorkoutCreateRequest, WorkoutCreateInternal, WorkoutReadFull, WorkoutReadBrief, WorkoutUserIDFilter



router = APIRouter()



@router.get("/workouts/users/{telegram_id}", response_model=List[WorkoutReadBrief])
async def get_workouts_by_user(
    telegram_id: int,
    session: AsyncSession = Depends(db.get_db)
):
    logger.info(f"Получение тренировок пользователя {telegram_id}")
    user = await UserDAO.find_one_or_none(session, filters=TelegramIDModel(telegram_id=telegram_id))
    if not user:
        raise HTTPException(404, detail="Пользователь не найден")
    
    workouts = await WorkoutDAO.find_all(
        session=session,
        filters=WorkoutUserIDFilter(user_id=user.id)
    )

    return workouts



@router.post("/users/{telegram_id}", response_model=WorkoutReadFull)
async def create_workout_for_user(
    telegram_id: int,
    workout: WorkoutCreateRequest,
    session: AsyncSession = Depends(db.get_db_with_commit)
):
    user = await UserDAO.find_one_or_none(session, filters=TelegramIDModel(telegram_id=telegram_id))
    if not user:
        raise HTTPException(404, detail="Пользователь не найден")
    user_id = user.id
    internal_data = WorkoutCreateInternal(
        user_id=user_id,
        workout_date=workout.workout_date,
        exercises=workout.exercises
    )
    new_workout = await WorkoutDAO.add_full_workout(session, internal_data)
    return WorkoutReadFull.model_validate(new_workout)



@router.get("/{workout_id}", response_model=WorkoutReadFull)
async def get_workout_by_id(workout_id: int, session: AsyncSession = Depends(db.get_db)):
    workout = await WorkoutDAO.get_full_by_id(session, workout_id)
    if not workout:
        raise HTTPException(404, detail="Тренировка не найдена")
    return WorkoutReadFull.model_validate(workout)


