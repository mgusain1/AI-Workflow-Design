from fastapi import APIRouter, Depends, HTTPException
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
        
def run_task(task_id:int ,db:Session):
    task = db.query(models.Task).filter(task_id==models.Task.id).first()
    if task is None:
        return
    task.status = "running"
    db.commit()
    if task.task_type == "summarize":
        task.result_text = f"Summary: {task.input_text[:80]}"
        task.status = "completed"
    else:
        task.status = "failed"
        task.error_message = "Unsupported task type"
    db.commit()
    db.refresh(task)
        
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
    run_task(new_task.id,db)
    db.refresh(new_task)
    return new_task

@router.get("/tasks/{task_id}",response_model=schemas.TaskResponse)
def get_task(task_id:int, db:Session=Depends(get_db)):
    task = db.query(models.Task).filter(task_id==models.Task.id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/tasks/{task_id}/result")
def get_task_result(task_id:int, db:Session=Depends(get_db)):
    task = db.query(models.Task).filter(task_id==models.Task.id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.status!="completed":
        return {
            "task id":task_id,
            "status":task.status,
            "result":"task not completed yet"
        }
    return {
        "task id":task_id,
        "status":task.status,
        "result":task.result_text
        }