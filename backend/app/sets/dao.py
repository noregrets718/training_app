
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.base import BaseDAO
from app.sets.models import Set



class SetDAO(BaseDAO):
    model = Set

    @classmethod
    async def get_by_workout_exercise_id(cls, session: AsyncSession, workout_exercise_id: int):
        result = await session.execute(
            select(cls.model)
            .where(cls.model.workout_exercise_id == workout_exercise_id)
            .order_by(cls.model.set_number)
        )
        return result.scalars().all()