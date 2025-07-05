from typing import List
from pydantic import BaseModel, ConfigDict
from app.exercises.schemas import ExerciseRead
from app.sets.schemas import SetRead



class WorkoutExerciseCreate(BaseModel):
    workout_id: int
    exercise_id: int
    number_of_sets: int


class WorkoutExerciseRead(BaseModel):
    id: int
    number_of_sets: int
    exercise: ExerciseRead  # ← связь на Exercise
    sets: List[SetRead]

    model_config = ConfigDict(from_attributes=True)