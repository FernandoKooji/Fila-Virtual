# ==========================================
# Mapeadores de resposta da API
# ==========================================

from app.utils.constants import STATUS_WAITING


def build_ticket_response(ticket):
    """
    Retorna um ticket simples.
    """

    return {
        "success": True,
        "id": ticket["id"],
        "ticket_code": ticket["ticket_code"],
        "ticket_type": ticket["ticket_type"],
        "status": ticket["status"]
    }


def build_current_ticket_response(ticket):
    """
    Resposta do atendimento atual.
    """

    return {
        "success": True,
        "id": ticket["id"],
        "ticket_code": ticket["ticket_code"],
        "ticket_type": ticket["ticket_type"],
        "status": ticket["status"],
        "called_at": ticket["called_at"]
    }


def build_position_response(ticket, position=None):
    """
    Resposta utilizada pelo Portal do Cliente.
    """

    response = {
        "success": True,
        "ticket_code": ticket["ticket_code"],
        "status": ticket["status"],
        "position": None,
        "people_ahead": None
    }

    if (
        ticket["status"] == STATUS_WAITING
        and position is not None
    ):

        response["position"] = position["position"]

        response["people_ahead"] = position["people_ahead"]

    return response


def build_message_response(message):
    """
    Resposta simples de sucesso.
    """

    return {
        "success": True,
        "message": message
    }