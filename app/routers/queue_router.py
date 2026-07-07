#===MODELOS===

#---fila---
from fastapi import APIRouter

#---finaliza atendimento---
from app.models.ticket import TicketFinish
from app.services.queue_service import (
    call_next,
    finish_ticket,
    get_current_ticket
)

#===ROTAS===

#---fila---
router = APIRouter(
    prefix="/queue",
    tags=["Queue"]
)

#---chama atual---
@router.get("/current")
def current_ticket_route():
    return get_current_ticket()

#---chama o proximo---
@router.post("/next")
def call_next_route():
    return call_next()

#---finaliza atendimento---
@router.post("/finish")
def finish_ticket_route(ticket: TicketFinish):
    return finish_ticket(ticket.id)