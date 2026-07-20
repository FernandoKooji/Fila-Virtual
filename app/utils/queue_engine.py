# ==========================================
# Queue Engine
# Regras de negócio da fila
# ==========================================

def sort_queue(waiting_tickets):
    """
    Ordena a fila conforme a regra atual:
    Todas as preferenciais primeiro,
    depois todas as normais.
    """

    priority = []
    normal = []

    for ticket in waiting_tickets:

        if ticket["ticket_type"] == "P":
            priority.append(ticket)

        else:
            normal.append(ticket)

    return priority + normal


def next_ticket(queue):
    """
    Retorna a próxima senha da fila.
    """

    if not queue:
        return None

    return queue[0]


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


def queue_statistics(queue):
    """
    Retorna estatísticas da fila.
    """

    priority = 0
    normal = 0

    for ticket in queue:

        if ticket["ticket_type"] == "P":
            priority += 1
        else:
            normal += 1

    return {
        "waiting_priority": priority,
        "waiting_normal": normal,
        "total_waiting": len(queue)
    }