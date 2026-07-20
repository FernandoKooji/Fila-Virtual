# ============================
# Imports
# ============================

from fastapi import APIRouter

from app.schemas.ticket import (
    FinishTicketRequest,
    MessageResponse
)

from app.schemas.queue import (
    CurrentTicketResponse,
    QueueStatusResponse,
    QueuePositionResponse
)

from app.services.queue_service import (
    get_ticket_position,
    call_next,
    finish_ticket,
    skip_ticket,
    cancel_ticket,
    get_current_ticket
)

# ============================
# Router
# ============================

router = APIRouter(
    prefix="/queue",
    tags=["Queue"]
)

# ============================
# Routes
# ============================

@router.get(
    "/current",
    response_model=CurrentTicketResponse
)
def current_ticket_route():
    return get_current_ticket()


@router.post("/next")
def call_next_route():
    return call_next()


@router.post(
    "/finish",
    response_model=MessageResponse
)
def finish_ticket_route(ticket: FinishTicketRequest):
    return finish_ticket(ticket.id)

@router.post(
    "/skip",
    response_model=MessageResponse
)
def skip_ticket_route(ticket: FinishTicketRequest):
    return skip_ticket(ticket.id)

@router.post(
    "/cancel",
    response_model=MessageResponse
)
def cancel_ticket_route(ticket: FinishTicketRequest):
    return cancel_ticket(ticket.id)

@router.get(
    "/position/{ticket_code}",
    response_model=QueuePositionResponse
)
def ticket_position_route(ticket_code: str):
    return get_ticket_position(ticket_code)