# models/pdf_document.py
from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class PDFDocument(Base):
    __tablename__ = 'pdf_documents'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    upload_date = Column(DateTime)
    file_path = Column(String, nullable=False)
