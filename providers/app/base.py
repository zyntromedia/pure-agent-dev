# app/providers/base.py
from abc import ABC, abstractmethod

class ComputeProvider(ABC):
    @abstractmethod
    async def create_instance(self, config: dict) -> dict:
        pass

    @abstractmethod
    async def delete_instance(self, instance_id: str) -> dict:
        pass
