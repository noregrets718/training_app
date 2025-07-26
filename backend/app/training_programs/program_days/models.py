from app.database import Base
from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, Text, DateTime, String, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ProgramDay(Base):
    __tablename__ = "program_days"

    id = mapped_column(Integer, primary_key=True)
    week_id = mapped_column(ForeignKey("program_weeks.id"))
    day_number = mapped_column(Integer)  # 1 — Пн, 2 — Вт и т.д.

    title = mapped_column(String, nullable=True)  # например "Грудь и спина"

    week = relationship("ProgramWeek", back_populates="days")
    exercises = relationship("ProgramExercise", back_populates="day", cascade="all, delete")