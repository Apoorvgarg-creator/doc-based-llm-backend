# models/answer_model.py
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class AnswerModel(Base):
    __tablename__ = 'answer_model'

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey('question_model.id'))

    # Establish a relationship with the QuestionModel
    question = relationship("QuestionModel", back_populates="answers")

    
