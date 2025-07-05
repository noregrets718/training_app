from typing import List
from sqlalchemy import Integer, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import  date
from app.database import Base
from app.workouts.models import Workout

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True)
    username: Mapped[str | None]
   
    # Relationships
    workouts: Mapped[List["Workout"]] = relationship(back_populates="user")