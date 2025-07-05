from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.session_maker_fast_api import db
from app.exercises.dao import ExerciseDAO
from app.exercises.schemas import ExerciseRead

router = APIRouter(prefix="/exercises", tags=["Exercises"])

@router.get("", response_model=List[ExerciseRead])
async def get_exercises(session: AsyncSession = Depends(db.get_db)):
    exercises = await ExerciseDAO.find_all(session=session)
    return exercises