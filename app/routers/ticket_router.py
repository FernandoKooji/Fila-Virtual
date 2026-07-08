from fastapi import APIRouter

from app.schemas.ticket import (
    CreateTicketRequest,
    TicketResponse
)

from app.services.ticket_service import create_ticket


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