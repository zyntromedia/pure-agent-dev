# app/schemas/task.py
from pydantic import BaseModel

class AgentTask(BaseModel):
    action: str
    parameters: dict
