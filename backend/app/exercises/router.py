from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.session_maker_fast_api import db
from app.exercises.dao import ExerciseDAO




router = APIRouter()




@router.get("/exercises")
async def get_exercises(
    session: AsyncSession = Depends(db.get_db)
):
    exercises = await ExerciseDAO.find_all(session=session)
    if not exercises:
        raise HTTPException(status_code=404, detail="User not found")
    return exercises