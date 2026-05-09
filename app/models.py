from sqlalchemy import Column, Integer, String, Text
from app.db import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    task_type = Column(String)
    status = Column(String)
    input_text = Column(Text)
    result_text = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)