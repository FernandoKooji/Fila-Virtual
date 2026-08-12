# ============================
# Imports
# ============================


from app.database.database import get_connection

from app.core.constants import (

    STATUS_IN_SERVICE,

    STATUS_WAITING

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
# Helpers
# ============================

def _get_cursor():

    connection = get_connection()

    return connection, connection.cursor()

def _get_ordered_queue(cursor):

    cursor.execute(

        GET_WAITING_TICKETS

    )

    waiting = cursor.fetchall()

    return sort_queue(waiting)

def _get_current_ticket(cursor):

    cursor.execute(

        GET_CURRENT_TICKET

    )

    return cursor.fetchone()

# ============================
# Atendimento atual
# ============================

def get_current_ticket():

    connection, cursor = _get_cursor()

    try:

        ticket = _get_current_ticket(cursor)
        
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

    connection, cursor = _get_cursor()

    try:

        ordered_queue = _get_ordered_queue(cursor)

        stats = queue_statistics(ordered_queue)

        ticket = _get_current_ticket(cursor)

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

    connection, cursor = _get_cursor()

    try:

        ordered_queue = _get_ordered_queue(cursor)

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

    connection, cursor = _get_cursor()

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

    connection, cursor = _get_cursor()

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

    connection, cursor = _get_cursor()

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

    connection, cursor = _get_cursor()

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

            ordered_queue = _get_ordered_queue(cursor)

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

    connection, cursor = _get_cursor()

    try:

        ordered = _get_ordered_queue(cursor)

        queue = [

            {

                "position": index,

                "id": ticket["id"],

                "ticket_code": ticket["ticket_code"],

                "ticket_type": ticket["ticket_type"]

            }

            for index, ticket in enumerate(

                ordered,

                start=1

            )

        ]

        return build_success_response({

            "queue": queue

        })

    finally:

        connection.close()

# ============================
# Rechamar senha
# ============================

def recall_ticket():

    connection, cursor = _get_cursor()

    try:

        ticket = _get_current_ticket(cursor)

        if ticket is None:

            no_current_ticket()

        return build_current_ticket_response(
            ticket
        )

    finally:

        connection.close()