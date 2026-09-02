# app/agents/executor.py
from app.providers.base import ComputeProvider
from app.schemas.task import AgentTask

class Executor:
    def __init__(self, provider: ComputeProvider):
        self.provider = provider

    async def execute(self, task: AgentTask) -> dict:
        if task.action == "create_instance":
            return await self.provider.create_instance(task.parameters)
        elif task.action == "delete_instance":
            return await self.provider.delete_instance(task.parameters["id"])
        else:
            raise ValueError("Unsupported task")
