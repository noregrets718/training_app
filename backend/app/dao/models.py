from datetime import datetime
from typing import Optional, List
from sqlalchemy import Integer, Text, ForeignKey, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import time, date
from app.dao.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True)
    username: Mapped[str | None]
   
    # Relationships
    workouts: Mapped[List["Workout"]] = relationship(back_populates="user")


class Workout(Base):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    day: Mapped[date] = mapped_column(nullable=False)


    #Relationships
    user: Mapped["User"] = relationship(back_populates="workouts")
    exercises: Mapped[List["WorkoutExercise"]] = relationship( back_populates='workout', cascade="all, delete-orphan")


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    #Relationships
    workout_exercises: Mapped[List["WorkoutExercise"]] = relationship( back_populates='exercise')



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


class Set(Base):
    __tablename__ = 'sets'

    id: Mapped[int] = mapped_column(primary_key=True)
    workout_exercise_id: Mapped[int] = mapped_column(ForeignKey("workout_exercises.id"))
    weight: Mapped[float] = mapped_column(nullable=False)
    repetitions: Mapped[int] = mapped_column(nullable=False)
    order:  Mapped[int] = mapped_column(nullable=False)

    #Relationships
    workout_exercise: Mapped[WorkoutExercise] = relationship(back_populates="sets")



