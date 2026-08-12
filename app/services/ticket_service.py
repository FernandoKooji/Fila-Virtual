# ============================
# Imports
# ============================

from app.database.database import get_connection

from app.core.constants import (
    NORMAL,
    PRIORITY,
    NORMAL_PREFIX,
    PRIORITY_PREFIX,
    STATUS_WAITING
)

from app.database.queries import (
    GET_LAST_NORMAL,
    GET_LAST_PRIORITY,
    UPDATE_LAST_NORMAL,
    UPDATE_LAST_PRIORITY,
    INSERT_TICKET,
    CANCEL_TICKET
)

from app.core.response_mapper import (
    build_ticket_response,
    build_message_response
)

from app.core.exceptions import (

    invalid_ticket_type,

    ticket_cannot_be_cancelled

)

TICKET_CONFIG = {

    NORMAL: {

        "get": GET_LAST_NORMAL,

        "update": UPDATE_LAST_NORMAL,

        "column": "last_normal_number",

        "prefix": NORMAL_PREFIX

    },

    PRIORITY: {

        "get": GET_LAST_PRIORITY,

        "update": UPDATE_LAST_PRIORITY,

        "column": "last_priority_number",

        "prefix": PRIORITY_PREFIX

    }

}

# ============================
# Functions
# ============================

def create_ticket(ticket_type):

    
    if ticket_type not in (NORMAL, PRIORITY):

        invalid_ticket_type()

    connection = get_connection()
    cursor = connection.cursor()

    try:

        
        if ticket_type == NORMAL:

            config = TICKET_CONFIG[NORMAL]

        else:

            config = TICKET_CONFIG[PRIORITY]

        
        cursor.execute(config["get"])

        result = cursor.fetchone()

        last_number = result[config["column"]]

        
        new_number = last_number + 1

        
        cursor.execute(
            config["update"],
            (new_number,)
        )

        
        ticket_code = f'{config["prefix"]}{new_number:03d}'

        
        cursor.execute(
            INSERT_TICKET,
            (
                ticket_code,
                ticket_type
            )
        )

        
        ticket_id = cursor.lastrowid

        connection.commit()

        ticket = {
            "id": ticket_id,
            "ticket_code": ticket_code,
            "ticket_type": ticket_type,
            "status": STATUS_WAITING
        }

        return build_ticket_response(ticket)

    finally:

        connection.close()

def cancel_ticket(ticket_code):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(

            CANCEL_TICKET,

            (ticket_code,)

        )

        if cursor.rowcount == 0:

            ticket_cannot_be_cancelled()

        connection.commit()

        return build_message_response(
            "Senha cancelada com sucesso."
        )

    finally:

        connection.close()