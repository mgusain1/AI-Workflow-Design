from pydantic import BaseModel

class TaskCreate(BaseModel):
    task_type: str
    input_text: str

class TaskResponse(BaseModel):
    id: int
    task_type: str
    status: str
    
    class config:
        from_attributes: True