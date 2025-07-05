from typing import List
from sqlalchemy import Integer, Text, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import  date
from app.database import Base
from app.workout_exercises.models import WorkoutExercise

class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    #Relationships
    workout_exercises: Mapped[List["WorkoutExercise"]] = relationship( back_populates='exercise')