from datetime import date, timedelta, datetime, time, timezone
from typing import List
from fastapi import HTTPException
from loguru import logger
from sqlalchemy import select, and_, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from app.dao.base import BaseDAO
from app.dao.models import User, Workout, WorkoutExercise, Exercise, Set
from app.api.schemas import WorkoutCreateUserModel, WorkoutCreateModel, WorkoutExerciseCreateModel, SetCreateModel, WorkoutTempReadModel, WorkoutExerciseReadModel


class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def get_user_id_by_tg_id(cls, session: AsyncSession, telegram_id: int) -> int | None:
        query = select(cls.model.id).filter_by(telegram_id =telegram_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()
    


            
class ExerciseDAO(BaseDAO):
    model = Exercise



class WorkoutExerciseDAO(BaseDAO):
    model = WorkoutExercise

    @classmethod
    async def get_by_workout_id(cls, session: AsyncSession, workout_id: int):
        result = await session.execute(
            select(cls.model).where(cls.model.workout_id == workout_id)
        )
        return result.scalars().all()
    

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
    


class WorkoutDAO(BaseDAO):
    model = Workout

    @classmethod
    async def get_by_user_id(cls, session: AsyncSession, user_id: int):
        result = await session.execute(
            select(cls.model).where(cls.model.user_id == user_id)
        )
        return result.scalars().all()
    

    @classmethod
    async def add_full_workout(cls, session: AsyncSession, workout_data: WorkoutCreateUserModel) -> Workout:
        try:
            # 1. Добавляем Workout через DAO
            workout: WorkoutTempReadModel = WorkoutTempReadModel.model_validate(
                await WorkoutDAO.add(session, WorkoutCreateModel(
                user_id=workout_data.user_id,
                day=workout_data.workout_date
            )))

            for exercise in workout_data.exercises:
                # 2. Добавляем WorkoutExercise через DAO
                workout_exercise: WorkoutExerciseReadModel = WorkoutExerciseReadModel.model_validate(
                    await WorkoutExerciseDAO.add(session, WorkoutExerciseCreateModel(
                    workout_id=workout.id,
                    exercise_id=exercise.exercise_id,
                    number_of_sets=len(exercise.sets)
                )))

                # 3. Добавляем Sets через DAO
                for i, s in enumerate(exercise.sets):
                    await SetDAO.add(session, SetCreateModel(
                        workout_exercise_id=workout_exercise.id,
                        weight=s.weight,
                        repetitions=s.repetitions,
                        order=i + 1
                    ))

            return workout

        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        
    @classmethod
    async def get_full_by_id(cls, session: AsyncSession, workout_id: int) -> Workout | None:
        logger.info(f"Получение тренировки с ID {workout_id} со всеми упражнениями и подходами")
        try:
            query = (
                select(cls.model)
                .options(
                    joinedload(cls.model.exercises)
                    .joinedload(WorkoutExercise.sets),
                    joinedload(cls.model.exercises)
                    .joinedload(WorkoutExercise.exercise)  # если хочешь получить названия упражнений
                )
                .filter(cls.model.id == workout_id)
            )
            result = await session.execute(query)
            workout = result.unique().scalar_one_or_none()  
            if workout:
                logger.info(f"Тренировка найдена: ID={workout.id}")
            else:
                logger.warning(f"Тренировка с ID={workout_id} не найдена")
            return workout
        except SQLAlchemyError as e:
            logger.error(f"Ошибка при получении тренировки ID={workout_id}: {e}")
            raise