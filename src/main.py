# main.py
from fastapi import FastAPI
from routes.pdf_routes import router as pdf_router
from routes.questions_routes import router as question_router
from database import engine, Base
from models import pdf_document
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})


# Define CORS origins to allow requests from all origins with credentials
# Replace "*" with your frontend's origin or list of allowed origins
origins = ["*"]

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


app.include_router(pdf_router)
app.include_router(question_router)

