# schema/pdf_schema.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PDFDocumentBase(BaseModel):
    filename: str
    upload_date: datetime
    file_path: str

class PDFDocumentCreate(PDFDocumentBase):
    pass

class PDFDocument(PDFDocumentBase):
    id: int

    class Config:
        orm_mode = True
