# app/providers/byteplus/ecs.py
from .base import ComputeProvider
from .client import BytePlusClient

class BytePlusECSProvider(ComputeProvider):
    def __init__(self):
        self.client = BytePlusClient()

    async def create_instance(self, config: dict) -> dict:
        return {"status": "created", "details": config}

    async def delete_instance(self, instance_id: str) -> dict:
        return {"status": "deleted", "id": instance_id}
