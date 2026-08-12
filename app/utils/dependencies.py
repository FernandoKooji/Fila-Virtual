# ==========================================
# Dependencies
# ==========================================

"""
Dependência compartilhada para fornecer
uma conexão com o banco utilizando
o mecanismo de Depends() do FastAPI.

Ainda não utilizada pelos Services,
mas mantida para futura expansão
da aplicação.
"""

from app.database.database import get_connection


def get_db():

    """
    Dependência para fornecer conexão com o banco.
    """

    connection = get_connection()

    try:

        yield connection

    finally:

        connection.close()