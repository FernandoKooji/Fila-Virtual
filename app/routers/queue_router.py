from fastapi import APIRouter

from app.services.queue_service import call_next

router = APIRouter(
    prefix="/queue",
    tags=["Queue"]
)

@router.post("/next")
def call_next_route():
    return call_next()