from fastapi import HTTPException


# ==========================================
# Função base (privada)
# ==========================================

def _http_error(status_code: int, message: str):
    """
    Cria uma HTTPException padronizada.
    """
    raise HTTPException(
        status_code=status_code,
        detail=message
    )


# ==========================================
# Erros genéricos
# ==========================================

def bad_request(message: str):
    _http_error(400, message)


def unauthorized(message: str = "Não autorizado."):
    _http_error(401, message)


def forbidden(message: str = "Acesso negado."):
    _http_error(403, message)


def not_found(message: str):
    _http_error(404, message)


def conflict(message: str):
    _http_error(409, message)


def internal_server_error(message: str = "Erro interno do servidor."):
    _http_error(500, message)


# ==========================================
# Sistema de Fila
# ==========================================

def queue_empty():
    not_found("Fila vazia.")


def no_current_ticket():
    not_found("Nenhum atendimento em andamento.")


def invalid_ticket_type():
    bad_request("Tipo de senha inválido.")


def ticket_not_found():
    not_found("Senha não encontrada.")


def ticket_not_found_or_not_in_service():
    not_found("Senha não encontrada ou não está em atendimento.")


def ticket_cannot_be_cancelled():
    conflict("Senha não encontrada ou não pode ser cancelada.")