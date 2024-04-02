from sqlalchemy.orm import Session
from models.question_model import QuestionModel
from schemas.question_schema import QuestionCreate


def save_question(db: Session, question: QuestionCreate):
    db_question = QuestionModel(text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question