# models/question_model.py
from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from sqlalchemy.orm import relationship

class QuestionModel(Base):
    __tablename__ = 'question_model'

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answers = relationship("AnswerModel", back_populates="question")
    
