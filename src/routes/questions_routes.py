# routes/upload_route.py
from fastapi import APIRouter
from controllers.questions_controller import answer_question

router = APIRouter()


router.post("/answer-question/")(answer_question)
