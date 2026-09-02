# app/services/compute_service.py
from app.agents.planner import Planner
from app.agents.executor import Executor
from app.providers.byteplus.ecs import BytePlusECSProvider

class ComputeService:
    def __init__(self):
        self.planner = Planner()
        self.executor = Executor(BytePlusECSProvider())

    async def handle_intent(self, intent: str) -> dict:
        task = self.planner.plan(intent)
        return await self.executor.execute(task)
