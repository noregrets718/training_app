from pydantic import BaseModel, ConfigDict



class ExerciseShortModel(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)




class ExerciseNameModel(BaseModel):
    name: str
