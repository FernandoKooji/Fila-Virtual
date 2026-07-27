# ==========================================
# Dependencies
# ==========================================

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