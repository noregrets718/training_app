from typing import List
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.workouts.models import Workout
from app.exercises.models import Exercise
from app.sets.models import Set

class WorkoutExercise(Base):

    __tablename__ = 'workout_exercises'

    id: Mapped[int] = mapped_column(primary_key=True)
    workout_id: Mapped[int] = mapped_column(ForeignKey("workouts.id"))
    exercise_id: Mapped[int] = mapped_column(ForeignKey("exercises.id"))
    number_of_sets: Mapped[int] = mapped_column(nullable=False)


    #Relationships
    workout: Mapped["Workout"] = relationship(back_populates="exercises")
    exercise: Mapped["Exercise"] = relationship(back_populates='workout_exercises')
    sets:  Mapped[List["Set"]] = relationship(back_populates="workout_exercise")