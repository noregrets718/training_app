from loguru import logger
from sqlalchemy import select, and_, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from app.dao.base import BaseDAO
from app.users.models import User

class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def get_user_id_by_tg_id(cls, session: AsyncSession, telegram_id: int) -> int | None:
        query = select(cls.model.id).filter_by(telegram_id =telegram_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()