# schemas/answer.py
from pydantic import BaseModel


class AnswerBase(BaseModel):
    answer: str


class AnswerCreate(AnswerBase):
    question_id: int


class Answer(AnswerBase):
    id: int
    question_id: int

    class Config:
        orm_mode = True
