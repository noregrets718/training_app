from pydantic import BaseModel, ConfigDict


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