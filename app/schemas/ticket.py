from pydantic import BaseModel


# ---------- Requests ----------

class CreateTicketRequest(BaseModel):
    ticket_type: str


class FinishTicketRequest(BaseModel):
    id: int


# ---------- Responses ----------

class TicketResponse(BaseModel):
    success: bool

    id: int

    ticket_code: str

    ticket_type: str

    status: str


class MessageResponse(BaseModel):
    success: bool

    message: str