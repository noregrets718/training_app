from pydantic import BaseModel, ConfigDict

class ExerciseCreate(BaseModel):
    name: str

class ExerciseRead(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
