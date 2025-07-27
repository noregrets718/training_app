from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
from typing import List

from app.dao.session_maker_fast_api import db
from app.users.dao import UserDAO
from app.users.schemas import TelegramIDModel
from app.programs.programs.dao import ProgramDao
from app.programs.programs.schemas import ProgramReadBrief, ProgramAuthorFilter
# from app.workouts.schemas import WorkoutCreateRequest, WorkoutCreateInternal, WorkoutReadFull, WorkoutReadBrief, WorkoutUserIDFilter



router = APIRouter(prefix="/programs", tags=["Programs"])







@router.get("/users/{telegram_id}", response_model=List[ProgramReadBrief])
async def get_program_by_user(
    telegram_id: int,
    session: AsyncSession = Depends(db.get_db)
):
    logger.info(f"Получение програм пользователя {telegram_id}")
    user = await UserDAO.find_one_or_none(session, filters=TelegramIDModel(telegram_id=telegram_id))
    if not user:
        raise HTTPException(404, detail="Пользователь не найден")
    
    programs = await ProgramDao.find_all(
        session=session,
        filters=ProgramAuthorFilter(author_id=user.id)
    )

    return programs
