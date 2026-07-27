# ==========================================
# Response Mapper
# Padronização das respostas da API
# ==========================================

from app.core.constants import STATUS_WAITING


# ==========================================
# Ticket
# ==========================================

def build_ticket_response(ticket):

    return {
        "success": True,
        "id": ticket["id"],
        "ticket_code": ticket["ticket_code"],
        "ticket_type": ticket["ticket_type"],
        "status": ticket["status"]
    }


# ==========================================
# Atendimento atual
# ==========================================

def build_current_ticket_response(ticket):

    return build_success_response({

        "id": ticket["id"],
        "ticket_code": ticket["ticket_code"],
        "ticket_type": ticket["ticket_type"],
        "status": ticket["status"],
        "called_at": ticket["called_at"]

    })


# ==========================================
# Consulta de posição
# ==========================================

def build_position_response(ticket, position=None):

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


# ==========================================
# Mensagem
# ==========================================

def build_message_response(message):

    return {

        "success": True,

        "message": message

    }


# ==========================================
# Erro
# ==========================================

def build_error_response(message):

    return {

        "success": False,

        "message": message

    }

# ==========================================
# Sucesso genérico
# ==========================================

def build_success_response(data=None):

    response = {
        "success": True
    }

    if data:
        response.update(data)

    return response