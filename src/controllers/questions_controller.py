# controllers/upload_controller.py
from fastapi import Depends, HTTPException, File
from pydantic import BaseModel
from sqlalchemy.orm import Session
from utils.startup_db import get_db
from utils.qa_utils import answer_question_util
import os
from datetime import datetime

class AnsQues(BaseModel):
    question: str
    filename: str

UPLOAD_FOLDER = "uploads" 

def answer_question(item: AnsQues, db: Session = Depends(get_db)):
    try:
       
        file_path = os.path.join(UPLOAD_FOLDER, item.filename)
        answer = answer_question_util(file_path, item.question, item.filename)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()