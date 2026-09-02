# app/api/routes/compute.py
from fastapi import APIRouter
from app.services.compute_service import ComputeService

router = APIRouter()
service = ComputeService()

@router.post("/compute")
async def compute(intent: str):
    return await service.handle_intent(intent)
