# ==========================================
# Imports
# ==========================================

from app.core.constants import PRIORITY


# ==========================================
# Queue Engine
# Regras de negócio da fila
# ==========================================

def sort_queue(waiting_tickets):

    """
    Ordena a fila conforme a regra atual:

    1. Todas as preferenciais
    2. Depois todas as normais
    """

    priority = []

    normal = []

    for ticket in waiting_tickets:

        if ticket["ticket_type"] == PRIORITY:

            priority.append(ticket)

        else:

            normal.append(ticket)

    return priority + normal


# ==========================================
# Próxima senha
# ==========================================

def next_ticket(queue):

    """
    Retorna a próxima senha da fila.
    """

    if not queue:

        return None

    return queue[0]


# ==========================================
# Posição da senha
# ==========================================

def ticket_position(queue, ticket_code):

    """
    Calcula a posição da senha.
    """

    for index, ticket in enumerate(queue):

        if ticket["ticket_code"] == ticket_code:

            return {

                "position": index + 1,

                "people_ahead": index

            }

    return None


# ==========================================
# Estatísticas da fila
# ==========================================

def queue_statistics(queue):

    """
    Retorna estatísticas da fila.
    """

    priority_count = 0

    normal_count = 0

    for ticket in queue:

        if ticket["ticket_type"] == PRIORITY:

            priority_count += 1

        else:

            normal_count += 1

    return {

        "waiting_priority": priority_count,

        "waiting_normal": normal_count,

        "total_waiting": len(queue)

    }