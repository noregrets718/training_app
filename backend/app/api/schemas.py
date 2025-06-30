from datetime import date, time
from typing import List, Dict, Text
from pydantic import BaseModel, ConfigDict





class TelegramIDModel(BaseModel):
    telegram_id: int

    model_config = ConfigDict(from_attributes=True)



class UserModel(TelegramIDModel):
    username: str | None


class ExerciseNameModel(BaseModel):
    name: str
    


class SetEntry(BaseModel):
    weight: float  # или int, если точно только целые
    repetitions: int


class ExerciseEntry(BaseModel):
    exercise_id: int
    sets: List[SetEntry]


class WorkoutFromClient(BaseModel):
    telegram_id: int
    workout_date: date  # или datetime
    exercises: List[ExerciseEntry]



class WorkoutCreateUserModel(BaseModel):
    user_id: int
    workout_date: date
    exercises: List[ExerciseEntry]
    


class WorkoutCreateModel(BaseModel):
    user_id: int
    day: date



class WorkoutTempReadModel(BaseModel):
    id: int
    user_id: int
    day: date  # как в SQLAlchemy-модели

    model_config = ConfigDict(from_attributes=True)






class WorkoutExerciseCreateModel(BaseModel):
    workout_id: int
    exercise_id: int
    number_of_sets: int



class WorkoutExerciseReadModel(BaseModel):
    id: int
    workout_id: int
    exercise_id: int
    number_of_sets: int

    model_config = ConfigDict(from_attributes=True)




class SetCreateModel(BaseModel):
    workout_exercise_id: int
    weight: float
    repetitions: int
    order: int


class SetReadModel(BaseModel):
    id: int
    weight: float
    repetitions: int
    order: int

    model_config =ConfigDict(from_attributes=True)


# --- Exercise внутри WorkoutExercise ---
# class ExerciseShortModel(BaseModel):
#     id: int
#     name: str

#     model_config = ConfigDict(from_attributes=True)


# # --- WorkoutExercise ---
# class WorkoutExerciseReadModel(BaseModel):
#     id: int
#     number_of_sets: int
#     exercise: ExerciseShortModel  # ← связь на Exercise
#     sets: List[SetReadModel]

#     model_config = ConfigDict(from_attributes=True)


# --- Workout ---
class WorkoutReadModel(BaseModel):
    id: int
    day: date
    exercises: List[WorkoutExerciseReadModel]

    model_config = ConfigDict(from_attributes=True)


