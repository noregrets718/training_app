from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.workout_exercises.models import WorkoutExercise

class Set(Base):
    __tablename__ = 'sets'

    id: Mapped[int] = mapped_column(primary_key=True)
    workout_exercise_id: Mapped[int] = mapped_column(ForeignKey("workout_exercises.id"))
    weight: Mapped[float] = mapped_column(nullable=False)
    repetitions: Mapped[int] = mapped_column(nullable=False)
    order:  Mapped[int] = mapped_column(nullable=False)

    #Relationships
    workout_exercise: Mapped[WorkoutExercise] = relationship(back_populates="sets")