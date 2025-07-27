from app.database import Base
from typing import List, TYPE_CHECKING, Optional
from sqlalchemy import ForeignKey, Integer, Text, DateTime, String, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, relationship



if TYPE_CHECKING:
    from app.programs.program_weeks.models import ProgramWeek
    from app.programs.program_exercises.models import ProgramExercise


class ProgramDay(Base):
    __tablename__ = "program_days"

    id: Mapped[int] = mapped_column(primary_key=True)
    week_id: Mapped[int] = mapped_column(ForeignKey("program_weeks.id"))
    day_number: Mapped[int] = mapped_column()  # 1 — Пн, 2 — Вт и т.д.
    title: Mapped[Optional[str]] = mapped_column(String, nullable=True)  # например "Грудь и спина"

    week: Mapped["ProgramWeek"] = relationship(back_populates="days")
    exercises: Mapped[List["ProgramExercise"]] = relationship(back_populates="day", cascade="all, delete")