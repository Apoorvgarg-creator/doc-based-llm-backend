# routes/upload_route.py
from fastapi import APIRouter
from controllers.pdf_controllers import upload_pdf
from schemas.pdf_schema import PDFDocument

router = APIRouter()

router.post("/upload/")(upload_pdf)
