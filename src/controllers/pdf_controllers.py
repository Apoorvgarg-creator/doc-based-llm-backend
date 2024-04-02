# controllers/upload_controller.py
from fastapi import Depends, UploadFile, HTTPException, File
from datetime import datetime
from sqlalchemy.orm import Session
from services.pdf_services import create_pdf_document
from schemas.pdf_schema import PDFDocumentCreate
from models.pdf_document import PDFDocument
from utils.startup_db import get_db
import os
import shutil
from datetime import datetime


UPLOAD_FOLDER = "uploads" 

def create_upload_folder():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

def upload_pdf(file: UploadFile = File(...),db: Session = Depends(get_db)):
    
    try:
        create_upload_folder()

        # Save the file to the local file system
        with open(os.path.join(UPLOAD_FOLDER, file.filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        pdf_data = PDFDocumentCreate(filename=file.filename,upload_date=datetime.now(), file_path=os.path.join(UPLOAD_FOLDER, file.filename))
        pdf_document = create_pdf_document(
            db=db,
            pdf_data=pdf_data
        )

        return {"id": pdf_document.id, "filename": pdf_document.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()