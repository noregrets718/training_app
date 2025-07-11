# from datetime import date
# from typing import List
# from pydantic import BaseModel, ConfigDict
# from app.workout_exercises.schemas import WorkoutExerciseReadModel




# class WorkoutTempReadModel(BaseModel):
#     id: int
#     user_id: int
#     day: date  # как в SQLAlchemy-модели

#     model_config = ConfigDict(from_attributes=True)



# class SetInput(BaseModel):
#     weight: float
#     repetitions: int



# class ExerciseInput(BaseModel):
#     exercise_id: int
#     sets: List[SetInput]



# class WorkoutCreateUserModel(BaseModel):
#     user_id: int
#     workout_date: date
#     exercises: List[ExerciseInput]



# class WorkoutCreateModel(BaseModel):
#     user_id: int
#     day: date



# class WorkoutFromClient(BaseModel):
#     telegram_id: int
#     workout_date: date  # или datetime
#     exercises: List[ExerciseInput]


# class WorkoutReadModel(BaseModel):
#     id: int
#     day: date
#     exercises: List[WorkoutExerciseReadModel]

#     model_config = ConfigDict(from_attributes=True)


from datetime import date
from typing import List
from pydantic import BaseModel, ConfigDict, Field
from app.workout_exercises.schemas import WorkoutExerciseRead

class SetInput(BaseModel):
    weight: float
    repetitions: int

class ExerciseInput(BaseModel):
    exercise_id: int
    sets: List[SetInput]


#Приходит от пользователя 
class WorkoutCreateRequest(BaseModel):
    workout_date: date
    title: str
    exercises: List[ExerciseInput]

#используется в методе дао как промежуточная модель
class WorkoutCreateInternal(BaseModel):
    user_id: int
    workout_date: date
    title: str
    exercises: List[ExerciseInput]

#использутеся для создания записи в бд 
class WorkoutCreate(BaseModel):
    user_id: int
    day: date = Field(alias="workout_date")
    title: str

    class Config:
        populate_by_name = True  


#используется в WorkoutList.vue для отображения списка тренировок
class WorkoutReadBrief(BaseModel):
    id: int
    day: date
    title: str

#используется для отображения полной тренировки при клике на нее
class WorkoutReadFull(WorkoutReadBrief):
    exercises: List[WorkoutExerciseRead]

    model_config = ConfigDict(from_attributes=True)


class WorkoutUserIDFilter(BaseModel):
    user_id: int