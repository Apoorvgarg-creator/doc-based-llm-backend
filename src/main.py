# main.py
from fastapi import FastAPI
from routes.pdf_routes import router as pdf_router
from routes.questions_routes import router as question_router
from database import engine, Base
from models import pdf_document

Base.metadata.create_all(bind=engine)
app = FastAPI(debug=True)

app.include_router(pdf_router)
app.include_router(question_router)

