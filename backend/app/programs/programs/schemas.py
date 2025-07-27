from datetime import date
from token import OP
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
# from app.workout_exercises.schemas import WorkoutExerciseRead


class ProgramReadBrief(BaseModel):
    id: int
    title: str

class ProgramAuthorFilter(BaseModel):
    author_id: int