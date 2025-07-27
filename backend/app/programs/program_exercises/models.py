from app.database import Base
from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, Text, DateTime, String, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from app.programs.program_days.models import ProgramDay
    from app.programs.program_sets.models import ProgramSet


class ProgramExercise(Base):
    __tablename__ = "program_exercises"

    id: Mapped[int] = mapped_column(primary_key=True)
    day_id: Mapped[int] = mapped_column(ForeignKey("program_days.id"))
    exercise_id: Mapped[int] = mapped_column(ForeignKey("exercises.id"))
    order: Mapped[int] = mapped_column()  # порядок отображения

    day: Mapped["ProgramDay"] = relationship(back_populates="exercises")
    sets: Mapped[List["ProgramSet"]] = relationship(back_populates="exercise", cascade="all, delete")