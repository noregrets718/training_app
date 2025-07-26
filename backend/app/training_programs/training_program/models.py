from app.database import Base
from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, Text, DateTime, String, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TrainingProgram(Base):
    __tablename__ = "training_programs"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    description = mapped_column(Text, nullable=True)
    author_id = mapped_column(ForeignKey("users.id"))  # автор программы
    is_public = mapped_column(Boolean, default=False)
    created_at = mapped_column(DateTime, default=func.now())

    weeks = relationship("ProgramWeek", back_populates="program", cascade="all, delete")