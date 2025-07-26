from app.database import Base
from sqlalchemy import ForeignKey, Integer, Float
from sqlalchemy.orm import mapped_column, relationship

class ProgramSet(Base):
    __tablename__ = "program_sets"

    id = mapped_column(Integer, primary_key=True)
    exercise_id = mapped_column(ForeignKey("program_exercises.id"))
    set_number = mapped_column(Integer)
    weight = mapped_column(Float)  # Вес
    reps = mapped_column(Integer)  # Повторения

    exercise = relationship("ProgramExercise", back_populates="sets")