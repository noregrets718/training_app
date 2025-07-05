from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.base import BaseDAO
from app.workout_exercises.models import WorkoutExercise



class WorkoutExerciseDAO(BaseDAO):
    model = WorkoutExercise

    @classmethod
    async def get_by_workout_id(cls, session: AsyncSession, workout_id: int):
        result = await session.execute(
            select(cls.model).where(cls.model.workout_id == workout_id)
        )
        return result.scalars().all()
    