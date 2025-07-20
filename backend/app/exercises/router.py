from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.session_maker_fast_api import db
from app.exercises.dao import ExerciseDAO
from app.exercises.schemas import ExerciseRead, ExerciseCreate
from app.exercises.schemas import ExerciseUpdate
from app.redis.exercise_cache import get_cached_exercises, set_cached_exercises, invalidate_cached_exercises

router = APIRouter(prefix="/exercises", tags=["Exercises"])

@router.get("", response_model=List[ExerciseRead])
async def get_exercises(session: AsyncSession = Depends(db.get_db)):
    cached = await get_cached_exercises()
    if cached:
        return cached
    
    exercises = await ExerciseDAO.find_all(session=session)
    await set_cached_exercises(exercises)
    return exercises



@router.post("", response_model=ExerciseRead)
async def create_exercise(data: ExerciseCreate, session: AsyncSession = Depends(db.get_db_with_commit)):
    exercise = await ExerciseDAO.add(session, data)
    await invalidate_cached_exercises()
    return exercise



@router.put("/{exercise_id}", response_model=ExerciseRead)
async def update_exercise(
    exercise_id: int,
    data: ExerciseUpdate,
    session: AsyncSession = Depends(db.get_db_with_commit)
):
    existing = await ExerciseDAO.find_one_or_none_by_id(exercise_id, session)
    if not existing:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    await ExerciseDAO.update(session, exercise_id, data)
    await invalidate_cached_exercises()
    # Получаем обновлённую запись и возвращаем
    return await ExerciseDAO.find_one_or_none_by_id(exercise_id, session)


@router.delete("/{exercise_id}")
async def delete_exercise(
    exercise_id: int,
    session: AsyncSession = Depends(db.get_db_with_commit)
):
    existing = await ExerciseDAO.find_one_or_none_by_id(exercise_id, session)
    if not existing:
        raise HTTPException(status_code=404, detail="Exercise not found")

    await ExerciseDAO.delete(session, exercise_id)
    await invalidate_cached_exercises()
    return {"detail": "Exercise deleted"}