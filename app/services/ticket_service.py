
#===IMPORTS===##

from app.database.database import get_connection

#---consulta senhas---
from app.database.queries import (
    GET_LAST_NORMAL,
    GET_LAST_PRIORITY,
    UPDATE_LAST_NORMAL,
    UPDATE_LAST_PRIORITY,
    INSERT_TICKET
)

def create_ticket(ticket_type):
    connection = get_connection()
    cursor = connection.cursor()

    #verifica tipo de senha
    if ticket_type == "N":
        config = {
            "get": GET_LAST_NORMAL,
            "update": UPDATE_LAST_NORMAL,
            "column": "last_normal_number",
            "prefix": "N"
        }
    else:
        config = {
            "get": GET_LAST_PRIORITY,
            "update": UPDATE_LAST_PRIORITY,
            "column": "last_priority_number",
            "prefix": "P"
        }

    # Executa o SELECT
    cursor.execute(config["get"])

    result = cursor.fetchone()

    last_number = result[config["column"]]

    new_number = last_number + 1

    cursor.execute(
        config["update"],
        (new_number,)
    )
    
    ticket_code = config["prefix"] + str(new_number).zfill(3)

    cursor.execute(
        INSERT_TICKET,
        (
            ticket_code,
            ticket_type
        )
    )

    connection.commit()
    connection.close()

    return {
        "ticket_code": ticket_code,
        "status": "aguardando"
    }




