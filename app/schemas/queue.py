from typing import Optional

from pydantic import BaseModel



class CurrentTicketResponse(BaseModel):
    success: bool
    id: Optional[int] = None
    ticket_code: Optional[str] = None
    ticket_type: Optional[str] = None
    status: Optional[str] = None
    called_at: Optional[str] = None


class QueueStatusResponse(BaseModel):
    success: bool

    current_ticket: str | None = None

    waiting_priority: int

    waiting_normal: int

    total_waiting: int


class QueuePositionResponse(BaseModel):

    success: bool

    ticket_code: str

    status: str

    position: Optional[int] = None

    people_ahead: Optional[int] = None


class QueueItem(BaseModel):

    position: int

    id: int

    ticket_code: str

    ticket_type: str


class QueueListResponse(BaseModel):

    success: bool

    queue: list[QueueItem]