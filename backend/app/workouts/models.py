from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import  date
from app.database import Base

if TYPE_CHECKING:
    from app.users.models import User
if TYPE_CHECKING:
    from app.workout_exercises.models import WorkoutExercise

class Workout(Base):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    day: Mapped[date] = mapped_column(nullable=False)


    #Relationships
    user: Mapped["User"] = relationship(back_populates="workouts")
    exercises: Mapped[List["WorkoutExercise"]] = relationship( back_populates='workout', cascade="all, delete-orphan")