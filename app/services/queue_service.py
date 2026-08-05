# ============================
# Imports
# ============================

from fastapi import HTTPException

from app.database.database import get_connection

from app.core.constants import (
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

from app.core.response_mapper import (
    build_success_response,
    build_ticket_response,
    build_current_ticket_response,
    build_position_response,
    build_message_response
)

from app.core.exceptions import (
    queue_empty,
    no_current_ticket,
    ticket_not_found,
    ticket_not_found_or_not_in_service,
    ticket_cannot_be_cancelled
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
            no_current_ticket()

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

        return build_success_response({

            "current_ticket": (
                current["ticket_code"]
                if current
                else None
            ),

            **stats

        })

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
            queue_empty()

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
            ticket_not_found_or_not_in_service()

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
            ticket_not_found_or_not_in_service()
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
            ticket_cannot_be_cancelled()

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

            ticket_not_found()

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

        ticket = dict(ticket)

        return build_position_response(ticket)

    finally:

        connection.close()

# ============================
# retorna a fila já ordenada
# ============================

def get_queue_list():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Busca todas as senhas aguardando
        cursor.execute(GET_WAITING_TICKETS)

        waiting = cursor.fetchall()

        # Ordena utilizando a regra da fila
        ordered = sort_queue(waiting)

        queue = []

        for index, ticket in enumerate(ordered, start=1):

            queue.append({

                "position": index,

                "id": ticket["id"],

                "ticket_code": ticket["ticket_code"],

                "ticket_type": ticket["ticket_type"]

            })

        return build_success_response({

            "queue": queue

        })

    finally:

        connection.close()

# ============================
# Rechamar senha
# ============================

def recall_ticket():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(GET_CURRENT_TICKET)

        ticket = cursor.fetchone()

        if ticket is None:

            not_found(
                "Nenhuma senha em atendimento."
            )

        return build_current_ticket_response(
            ticket
        )

    finally:

        connection.close()