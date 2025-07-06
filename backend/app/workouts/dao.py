
# from loguru import logger
# from sqlalchemy import select, and_, func
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import joinedload
# from app.dao.base import BaseDAO
# from app.workouts.models import Workout
# from app.workout_exercises.models import WorkoutExercise
# from app.workouts.schemas import WorkoutTempReadModel, WorkoutCreateUserModel, WorkoutCreateModel
# from app.workout_exercises.dao import WorkoutExerciseDAO
# from app.workout_exercises.schemas import WorkoutExerciseCreateModel
# from app.sets.dao import SetDAO
# from app.sets.schemas import SetCreateModel

# class WorkoutDAO(BaseDAO):
#     model = Workout

#     @classmethod
#     async def get_by_user_id(cls, session: AsyncSession, user_id: int):
#         result = await session.execute(
#             select(cls.model).where(cls.model.user_id == user_id)
#         )
#         return result.scalars().all()
    

#     @classmethod
#     async def add_full_workout(cls, session: AsyncSession, workout_data: WorkoutCreateUserModel) -> Workout:
#         try:
#             # 1. Добавляем Workout через DAO
#             workout: WorkoutTempReadModel = WorkoutTempReadModel.model_validate(
#                 await WorkoutDAO.add(session, WorkoutCreateModel(
#                 user_id=workout_data.user_id,
#                 day=workout_data.workout_date
#             )))

#             for exercise in workout_data.exercises:
#                 # 2. Добавляем WorkoutExercise через DAO
#                 workout_exercise = await WorkoutExerciseDAO.add(session, WorkoutExerciseCreateModel(
#                 workout_id=workout.id,
#                 exercise_id=exercise.exercise_id,
#                 number_of_sets=len(exercise.sets)
                
#             ))

#                 # 3. Добавляем Sets через DAO
#                 for i, s in enumerate(exercise.sets):
#                     await SetDAO.add(session, SetCreateModel(
#                         workout_exercise_id=workout_exercise.id,
#                         weight=s.weight,
#                         repetitions=s.repetitions,
#                         order=i + 1
#                     ))

#             return workout

#         except SQLAlchemyError as e:
#             await session.rollback()
#             raise e
        
#     @classmethod
#     async def get_full_by_id(cls, session: AsyncSession, workout_id: int) -> Workout | None:
#         logger.info(f"Получение тренировки с ID {workout_id} со всеми упражнениями и подходами")
#         try:
#             query = (
#                 select(cls.model)
#                 .options(
#                     joinedload(cls.model.exercises)
#                     .joinedload(WorkoutExercise.sets),
#                     joinedload(cls.model.exercises)
#                     .joinedload(WorkoutExercise.exercise)  # если хочешь получить названия упражнений
#                 )
#                 .filter(cls.model.id == workout_id)
#             )
#             result = await session.execute(query)
#             workout = result.unique().scalar_one_or_none()  
#             if workout:
#                 logger.info(f"Тренировка найдена: ID={workout.id}")
#             else:
#                 logger.warning(f"Тренировка с ID={workout_id} не найдена")
#             return workout
#         except SQLAlchemyError as e:
#             logger.error(f"Ошибка при получении тренировки ID={workout_id}: {e}")
#             raise
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.exc import SQLAlchemyError
from loguru import logger

from app.dao.base import BaseDAO
from app.workouts.models import Workout
from app.workout_exercises.dao import WorkoutExerciseDAO
from app.sets.dao import SetDAO
from app.sets.schemas import SetCreate
from app.workout_exercises.models import WorkoutExercise
from app.workout_exercises.schemas import WorkoutExerciseCreate
from app.workouts.schemas import WorkoutCreateInternal, WorkoutCreate
from pydantic import BaseModel



class WorkoutDAO(BaseDAO):
    model = Workout



    @classmethod
    async def add_full_workout(cls, session: AsyncSession, data: WorkoutCreateInternal) -> Workout:
        values = WorkoutCreate.model_validate(data.model_dump(exclude={"exercises"}))
        try:
            workout = await cls.add(session, values)

            for exercise in data.exercises:
                workout_exercise = await WorkoutExerciseDAO.add(session, WorkoutExerciseCreate(
                    workout_id=workout.id,
                    exercise_id=exercise.exercise_id,
                    number_of_sets=len(exercise.sets)
                ))

                for order, s in enumerate(exercise.sets, start=1):
                    await SetDAO.add(session, SetCreate(
                        workout_exercise_id=workout_exercise.id,
                        weight=s.weight,
                        repetitions=s.repetitions,
                        order=order
                    ))

                stmt = (
                select(cls.model)
                .options(
                    joinedload(cls.model.exercises).joinedload(WorkoutExercise.sets),
                    joinedload(cls.model.exercises).joinedload(WorkoutExercise.exercise)
                )
                .filter(cls.model.id == workout.id)
            )
            result = await session.execute(stmt)
            workout_with_exercises = result.scalar_one()

            return workout_with_exercises


        except SQLAlchemyError as e:
            await session.rollback()
            raise e



    @classmethod
    async def get_full_by_id(cls, session: AsyncSession, workout_id: int) -> Workout | None:
        query = (
            select(cls.model)
            .options(
                joinedload(cls.model.exercises).joinedload(WorkoutExercise.sets),
                joinedload(cls.model.exercises).joinedload(WorkoutExercise.exercise)
            )
            .filter(cls.model.id == workout_id)
        )
        result = await session.execute(query)
        return result.unique().scalar_one_or_none()
