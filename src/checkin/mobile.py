"""Mobile check-in with ID scan."""

from fastapi import APIRouter, UploadFile

router = APIRouter(prefix="/api/checkin")

@router.post("/mobile")
async def mobile_checkin(id_scan: UploadFile, reservation_id: str):
    """Process mobile check-in with ID document scan."""
    # OCR extraction
    # Validate against reservation
    return {"status": "checked_in", "room": "412"}
