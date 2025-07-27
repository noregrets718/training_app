from app.database import Base
from typing import List, TYPE_CHECKING, Optional
from datetime import datetime
from sqlalchemy import ForeignKey, Integer, Text,  func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.programs.program_weeks.models import ProgramWeek

class Program(Base):
    __tablename__ = "training_programs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    is_public: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now())

    weeks: Mapped[List["ProgramWeek"]] = relationship(back_populates="program", cascade="all, delete")