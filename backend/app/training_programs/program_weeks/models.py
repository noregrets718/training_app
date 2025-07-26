from app.database import Base

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ProgramWeek(Base):
    __tablename__ = "program_weeks"

    id = mapped_column(Integer, primary_key=True)
    program_id = mapped_column(ForeignKey("training_programs.id"))
    week_number = mapped_column(Integer)  # 1, 2, 3, ...

    program = relationship("TrainingProgram", back_populates="weeks")
    days = relationship("ProgramDay", back_populates="week", cascade="all, delete")