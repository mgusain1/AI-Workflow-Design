from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db : Session = Depends(get_db)):
    new_task = models.Task(
        task_type = task.task_type,
        input_text = task.input_text,
        status="pending"
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/tasks/{task_id}",response_model=schemas.TaskResponse)
def get_task(task_id:int, db:Session=Depends(get_db)):
    task = db.query(models.Task).filter(task_id==models.Task.id).first()
    return task
