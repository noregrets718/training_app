from typing import List
from pydantic import BaseModel, ConfigDict
from app.exercises.schemas import ExerciseShortModel
from app.sets.schemas import SetReadModel



class WorkoutExerciseCreateModel(BaseModel):
    workout_id: int
    exercise_id: int
    number_of_sets: int


class WorkoutExerciseReadModel(BaseModel):
    id: int
    number_of_sets: int
    exercise: ExerciseShortModel  # ← связь на Exercise
    sets: List[SetReadModel]

    model_config = ConfigDict(from_attributes=True)