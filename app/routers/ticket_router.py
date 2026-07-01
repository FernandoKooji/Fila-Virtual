from fastapi import APIRouter

from app.models.ticket import TicketCreate
from app.services.ticket_service import create_ticket

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@router.post("/")
def create_ticket_route(ticket: TicketCreate):
    return create_ticket(ticket.ticket_type)