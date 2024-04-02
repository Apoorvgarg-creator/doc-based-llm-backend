from sqlalchemy.orm import Session
from models.answer_model import AnswerModel
from schemas.answer_schema import AnswerCreate


def save_answer(db: Session, answer: AnswerCreate):
    db_answer = AnswerModel(text=answer.text)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer