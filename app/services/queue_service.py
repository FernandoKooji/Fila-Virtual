#===IMPORTS===

from app.database.database import get_connection

#---consulta senhas---
from app.database.queries import (
    GET_NEXT_PRIORITY,
    GET_NEXT_NORMAL,
    CALL_TICKET
)

#---funcao chama proximo---

def call_next():

    #procura preferencial
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(GET_NEXT_PRIORITY)

    ticket = cursor.fetchone()

    if ticket is None:

        #procura normal
        cursor.execute(GET_NEXT_NORMAL)

        ticket = cursor.fetchone()

    if ticket is None:
        connection.close()

        return {
            "message": "Fila vazia"
        }

    #localiza id
    cursor.execute(
        CALL_TICKET,
        (ticket["id"],)
    )

    connection.commit()
    connection.close()

    return {
        "ticket_code": ticket["ticket_code"],
        "ticket_type": ticket["ticket_type"],
        "status": "em_atendimento"
    }
