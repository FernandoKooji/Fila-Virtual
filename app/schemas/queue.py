from typing import Optional
from pydantic import BaseModel


class CurrentTicketResponse(BaseModel):
    success: bool
    id: Optional[int] = None
    ticket_code: Optional[str] = None
    ticket_type: Optional[str] = None
    status: Optional[str] = None
    called_at: Optional[str] = None