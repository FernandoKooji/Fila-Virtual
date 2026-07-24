# ============================
# Imports
# ============================

from fastapi import HTTPException

from app.database.database import get_connection

from app.utils.constants import (
    STATUS_IN_SERVICE,
    STATUS_FINISHED,
    STATUS_WAITING,
    STATUS_ABSENT,
    STATUS_CANCELLED
)

from app.database.queries import (
    GET_TICKET,
    GET_WAITING_TICKETS,
    GET_CURRENT_TICKET,
    CALL_TICKET,
    FINISH_TICKET,
    SKIP_TICKET,
    CANCEL_TICKET
)

from app.utils.queue_engine import (
    sort_queue,
    next_ticket,
    ticket_position,
    queue_statistics
)

from app.utils.ticket_mapper import (
    build_current_ticket_response,
    build_position_response,
    build_message_response,
    build_ticket_response
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

        return build_current_ticket_response(ticket)

    finally:

        connection.close()

# ============================
# Resumo da fila
# ============================

"""
Ela responde perguntas como:

Qual senha está em atendimento?
Quantas senhas preferenciais estão aguardando?
Quantas senhas normais estão aguardando?
Quantas pessoas há na fila ao todo?
"""

def get_queue_status():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Busca todas as senhas aguardando
        cursor.execute(GET_WAITING_TICKETS)
        waiting = cursor.fetchall()

        ordered_queue = sort_queue(waiting)

        stats = queue_statistics(ordered_queue)

        # Busca atendimento atual
        cursor.execute(GET_CURRENT_TICKET)
        current = cursor.fetchone()

        return {
            "success": True,
            "current_ticket": (
                current["ticket_code"]
                if current
                else None
            ),
            **stats
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

        cursor.execute(GET_WAITING_TICKETS)

        waiting_tickets = cursor.fetchall()

        ordered_queue = sort_queue(waiting_tickets)

        ticket = next_ticket(ordered_queue)

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

        ticket = dict(ticket)

        ticket["status"] = STATUS_IN_SERVICE

        return build_ticket_response(ticket)
    
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

        return build_message_response(
            "Atendimento finalizado."
        )

    finally:

        connection.close()

# ============================
# Pular senha atual "ausente"
# ============================

def skip_ticket(ticket_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            SKIP_TICKET,
            (ticket_id,)
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Senha não encontrada ou não está em atendimento."
            )

        connection.commit()

        return build_message_response(
            "Senha marcada como ausente."
        )

    finally:

        connection.close()

# ============================
# Cancelar senha (cliente)
# ============================

def cancel_ticket(ticket_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            CANCEL_TICKET,
            (ticket_id,)
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Senha não encontrada ou não pode ser cancelada."
            )

        connection.commit()

        return build_message_response(
            "Senha cancelada com sucesso."
        )

    finally:

        connection.close()

# ============================
# Consulta posicao de senha (cliente)
# ============================

def get_ticket_position(ticket_code):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Procura o ticket independentemente do status
        cursor.execute(
            GET_TICKET,
            (ticket_code,)
        )

        ticket = cursor.fetchone()

        if ticket is None:

            raise HTTPException(
                status_code=404,
                detail="Senha não encontrada."
            )

        # Apenas aguardando possui posição
        if ticket["status"] == STATUS_WAITING:

            cursor.execute(GET_WAITING_TICKETS)

            waiting = cursor.fetchall()

            ordered_queue = sort_queue(waiting)

            position = ticket_position(
                ordered_queue,
                ticket_code
            )

            ticket = dict(ticket)

            return build_position_response(
                ticket,
                position
            )

        # Todos os demais estados
        return build_position_response(ticket)

    finally:

        connection.close()