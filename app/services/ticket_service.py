from fastapi import HTTPException

from app.database.database import get_connection

from app.database.queries import (
    GET_LAST_NORMAL,
    GET_LAST_PRIORITY,
    UPDATE_LAST_NORMAL,
    UPDATE_LAST_PRIORITY,
    INSERT_TICKET
)


def create_ticket(ticket_type):

    # Valida o tipo de senha antes de acessar o banco
    if ticket_type not in ("N", "P"):
        raise HTTPException(
            status_code=400,
            detail="Tipo de senha inválido."
        )

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Configuração conforme o tipo da senha
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

        # Busca o último número utilizado
        cursor.execute(config["get"])

        result = cursor.fetchone()

        last_number = result[config["column"]]

        # Gera o próximo número
        new_number = last_number + 1

        # Atualiza o contador
        cursor.execute(
            config["update"],
            (new_number,)
        )

        # Monta o código da senha
        ticket_code = (
            config["prefix"] +
            str(new_number).zfill(3)
        )

        # Salva o ticket
        cursor.execute(
            INSERT_TICKET,
            (
                ticket_code,
                ticket_type
            )
        )

        # Obtém o ID criado
        ticket_id = cursor.lastrowid

        connection.commit()

        return {
            "success": True,
            "id": ticket_id,
            "ticket_code": ticket_code,
            "ticket_type": ticket_type,
            "status": "aguardando"
        }

    finally:

        connection.close()