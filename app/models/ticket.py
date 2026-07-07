from pydantic import BaseModel

#===requisicoes===

#---cria tipo de senha---

class TicketCreate(BaseModel):
    ticket_type: str

#---finalizar atendimento---

class TicketFinish(BaseModel):
    id: int