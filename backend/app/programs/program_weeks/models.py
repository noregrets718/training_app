from app.database import Base
from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.programs.programs.models import Program
    from app.programs.program_days.models import ProgramDay


class ProgramWeek(Base):
    __tablename__ = "program_weeks"

    id: Mapped[int] = mapped_column(primary_key=True)
    program_id: Mapped[int] = mapped_column(ForeignKey("training_programs.id"))
    week_number: Mapped[int] = mapped_column()

    program: Mapped["Program"] = relationship(back_populates="weeks")
    days: Mapped[List["ProgramDay"]] = relationship(back_populates="week", cascade="all, delete")