# ============================
# Imports
# ============================

from fastapi import APIRouter

from app.schemas.ticket import (
    CreateTicketRequest,
    TicketResponse,
    MessageResponse
)

from app.services.ticket_service import (
    create_ticket,
    cancel_ticket
)

# ============================
# Routes
# ============================

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@router.post(
    "/",
    response_model=TicketResponse
)
def create_ticket_route(ticket: CreateTicketRequest):
    return create_ticket(ticket.ticket_type)

@router.delete(
    "/{ticket_code}",
    response_model=MessageResponse
)
def cancel_ticket_route(ticket_code: str):

    return cancel_ticket(ticket_code)