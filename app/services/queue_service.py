# ============================
# Imports
# ============================

from fastapi import HTTPException

from app.database.database import get_connection

from app.database.queries import (
    FINISH_TICKET,
    GET_CURRENT_TICKET,
    GET_NEXT_PRIORITY,
    GET_NEXT_NORMAL,
    CALL_TICKET
)


# ============================
# Atendimento atual
# ============================

def get_current_ticket():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(GET_CURRENT_TICKET)

        ticket = cursor.fetchone()

        if ticket is None:
            raise HTTPException(
                status_code=404,
                detail="Nenhum atendimento em andamento."
            )

        return {
            "success": True,
            "id": ticket["id"],
            "ticket_code": ticket["ticket_code"],
            "ticket_type": ticket["ticket_type"],
            "status": ticket["status"],
            "called_at": ticket["called_at"]
        }

    finally:

        connection.close()


# ============================
# Chamar próxima senha
# ============================

def call_next():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Procura senha preferencial
        cursor.execute(GET_NEXT_PRIORITY)

        ticket = cursor.fetchone()

        # Caso não exista, procura senha normal
        if ticket is None:

            cursor.execute(GET_NEXT_NORMAL)

            ticket = cursor.fetchone()

        # Nenhuma senha aguardando
        if ticket is None:
            raise HTTPException(
                status_code=404,
                detail="Fila vazia."
            )

        # Atualiza o status da senha
        cursor.execute(
            CALL_TICKET,
            (ticket["id"],)
        )

        connection.commit()

        return {
            "success": True,
            "id": ticket["id"],
            "ticket_code": ticket["ticket_code"],
            "ticket_type": ticket["ticket_type"],
            "status": "em_atendimento"
        }

    finally:

        connection.close()


# ============================
# Finalizar atendimento
# ============================

def finish_ticket(ticket_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            FINISH_TICKET,
            (ticket_id,)
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Senha não encontrada ou não está em atendimento."
            )

        connection.commit()

        return {
            "success": True,
            "message": "Atendimento finalizado."
        }

    finally:

        connection.close()