from app.database import Base
from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from app.programs.program_exercises.models import ProgramExercise

class ProgramSet(Base):
    __tablename__ = "program_sets"

    id: Mapped[int] = mapped_column(primary_key=True)
    exercise_id: Mapped[int] = mapped_column(ForeignKey("program_exercises.id"))
    set_number: Mapped[int] = mapped_column()
    weight: Mapped[float] = mapped_column()
    reps: Mapped[int] = mapped_column()

    exercise: Mapped["ProgramExercise"] = relationship(back_populates="sets")