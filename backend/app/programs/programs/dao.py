from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.exc import SQLAlchemyError
from loguru import logger

from app.dao.base import BaseDAO
from app.programs.programs.models import Program

class ProgramDao(BaseDAO):
    model = Program