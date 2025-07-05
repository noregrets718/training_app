from pydantic import BaseModel, ConfigDict


class SetCreate(BaseModel):
    workout_exercise_id: int
    weight: float
    repetitions: int
    order: int


class SetRead(BaseModel):
    id: int
    weight: float
    repetitions: int
    order: int

    model_config =ConfigDict(from_attributes=True)