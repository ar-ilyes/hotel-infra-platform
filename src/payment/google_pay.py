"""Google Pay integration."""

from fastapi import APIRouter

router = APIRouter(prefix="/api/payment")

@router.post("/google-pay")
async def process_google_pay(token: str, amount: float):
    return {"status": "success", "provider": "google_pay"}
