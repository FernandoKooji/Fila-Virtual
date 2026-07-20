from typing import Optional

from pydantic import BaseModel


# ============================
# Atendimento Atual
# ============================

class CurrentTicketResponse(BaseModel):
    success: bool
    id: Optional[int] = None
    ticket_code: Optional[str] = None
    ticket_type: Optional[str] = None
    status: Optional[str] = None
    called_at: Optional[str] = None


# ============================
# Resumo da fila
# ============================

class QueueStatusResponse(BaseModel):
    success: bool

    current_ticket: str | None = None

    waiting_priority: int

    waiting_normal: int

    total_waiting: int

# ============================
# Posição da senha
# ============================

class QueuePositionResponse(BaseModel):
    success: bool
    ticket_code: str
    status: str
    position: int
    people_ahead: int