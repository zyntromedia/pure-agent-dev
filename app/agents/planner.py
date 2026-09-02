# app/agents/planner.py
from app.schemas.task import AgentTask

class Planner:
    def plan(self, intent: str) -> AgentTask:
        return AgentTask(action="create_instance", parameters={"size": "medium"})
