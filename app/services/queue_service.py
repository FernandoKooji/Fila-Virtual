#===IMPORTS===

from app.database.database import get_connection

#---consulta senhas---
from app.database.queries import (
    FINISH_TICKET,
    GET_CURRENT_TICKET,
    GET_NEXT_PRIORITY,
    GET_NEXT_NORMAL,
    CALL_TICKET
)

#===FUNCOES===

#---funcao chama atual---
def get_current_ticket():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(GET_CURRENT_TICKET)
    ticket = cursor.fetchone()

    if ticket is None:
        connection.close()

        return {
            "success": False,
            "message": "Nenhum atendimento em andamento."
        }

    connection.close()

    return {
        "success": True,
        "ticket": {
            "id": ticket["id"],
            "ticket_code": ticket["ticket_code"],
            "ticket_type": ticket["ticket_type"],
            "status": ticket["status"],
            "called_at": ticket["called_at"]
        }
    } 



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
        "id": ticket["id"],
        "ticket_code": ticket["ticket_code"],
        "ticket_type": ticket["ticket_type"],
        "status": "em_atendimento"
    }

#---funcao finaliza atendimento---
def finish_ticket(ticket_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        FINISH_TICKET,
        (ticket_id,)
    )

    if cursor.rowcount == 0:

        connection.close()

        return {
            "success": False,
            "message": "Senha não encontrada ou não está em atendimento."
        }

    connection.commit()
    connection.close()

    return {
        "success": True,
        "message": "Atendimento finalizado."
    }