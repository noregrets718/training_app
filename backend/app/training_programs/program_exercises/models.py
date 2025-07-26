from app.database import Base
from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, Text, DateTime, String, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ProgramExercise(Base):
    __tablename__ = "program_exercises"

    id = mapped_column(Integer, primary_key=True)
    day_id = mapped_column(ForeignKey("program_days.id"))
    exercise_id = mapped_column(ForeignKey("exercises.id"))  # связь с глобальной таблицей упражнений
    order = mapped_column(Integer)  # порядок отображения

    day = relationship("ProgramDay", back_populates="exercises")
    sets = relationship("ProgramSet", back_populates="exercise", cascade="all, delete")