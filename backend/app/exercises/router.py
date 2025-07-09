from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.session_maker_fast_api import db
from app.exercises.dao import ExerciseDAO
from app.exercises.schemas import ExerciseRead, ExerciseCreate
from app.exercises.schemas import ExerciseUpdate

router = APIRouter(prefix="/exercises", tags=["Exercises"])

@router.get("", response_model=List[ExerciseRead])
async def get_exercises(session: AsyncSession = Depends(db.get_db)):
    exercises = await ExerciseDAO.find_all(session=session)
    return exercises



@router.post("", response_model=ExerciseRead)
async def create_exercise(data: ExerciseCreate, session: AsyncSession = Depends(db.get_db_with_commit)):
    return await ExerciseDAO.add(session, data)



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
    return {"detail": "Exercise deleted"}