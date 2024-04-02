# services/pdf_service.py
from sqlalchemy.orm import Session
from models.pdf_document import PDFDocument
from schemas.pdf_schema import PDFDocumentCreate
from datetime import datetime
from utils import extract_text
import shutil

def get_pdf_by_filename(db: Session, filename: str):
    return db.query(PDFDocument).filter(PDFDocument.filename == filename).first()


def create_pdf_document(db: Session, pdf_data: PDFDocumentCreate):
    # Check if the filename already exists
    existing_pdf = get_pdf_by_filename(db, pdf_data.filename)
    if existing_pdf:
        raise ValueError("Filename already exists")

    file_content = extract_text.extract_pdf_content(pdf_data.file_path)
    if file_content:
        # Create the PDF document in the database
        db_pdf = PDFDocument(filename = pdf_data.filename, upload_date=pdf_data.upload_date, file_path=pdf_data.file_path)
        db.add(db_pdf)
        db.commit()
        db.refresh(db_pdf) 
        return db_pdf
    else:
        print("Failed to extract PDF content.")
        raise ValueError("Failed to extract PDF content.")
        