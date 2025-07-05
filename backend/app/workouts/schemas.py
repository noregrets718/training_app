from datetime import date
from typing import List
from pydantic import BaseModel, ConfigDict
from app.workout_exercises.schemas import WorkoutExerciseReadModel



class WorkoutTempReadModel(BaseModel):
    id: int
    user_id: int
    day: date  # как в SQLAlchemy-модели

    model_config = ConfigDict(from_attributes=True)



class SetEntry(BaseModel):
    weight: float  # или int, если точно только целые
    repetitions: int



class ExerciseEntry(BaseModel):
    exercise_id: int
    sets: List[SetEntry]



class WorkoutCreateUserModel(BaseModel):
    user_id: int
    workout_date: date
    exercises: List[ExerciseEntry]



class WorkoutCreateModel(BaseModel):
    user_id: int
    day: date



class WorkoutFromClient(BaseModel):
    telegram_id: int
    workout_date: date  # или datetime
    exercises: List[ExerciseEntry]


class WorkoutReadModel(BaseModel):
    id: int
    day: date
    exercises: List[WorkoutExerciseReadModel]

    model_config = ConfigDict(from_attributes=True)


