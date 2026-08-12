# ============================
# Contadores
# ============================

GET_LAST_NORMAL = """
SELECT last_normal_number
FROM system_state
WHERE id = 1;
"""

GET_LAST_PRIORITY = """
SELECT last_priority_number
FROM system_state
WHERE id = 1;
"""

UPDATE_LAST_NORMAL = """
UPDATE system_state
SET last_normal_number = ?
WHERE id = 1;
"""

UPDATE_LAST_PRIORITY = """
UPDATE system_state
SET last_priority_number = ?
WHERE id = 1;
"""

# ============================
# Tickets
# ============================

INSERT_TICKET = """
INSERT INTO tickets (
    ticket_code,
    ticket_type,
    status,
    created_at
)
VALUES (
    ?,
    ?,
    'aguardando',
    datetime('now', 'localtime')
);
"""

GET_TICKET = """
SELECT
    id,
    ticket_code,
    ticket_type,
    status,
    created_at,
    called_at,
    finished_at
FROM tickets
WHERE ticket_code = ?;
"""

GET_WAITING_TICKETS = """
SELECT
    id,
    ticket_code,
    ticket_type,
    status,
    created_at
FROM tickets
WHERE status = 'aguardando'
ORDER BY created_at;
"""

GET_CURRENT_TICKET = """
SELECT
    id,
    ticket_code,
    ticket_type,
    status,
    called_at
FROM tickets
WHERE status = 'em_atendimento'
ORDER BY called_at DESC
LIMIT 1;
"""

# ============================
# Mudanca de status
# ============================

CALL_TICKET = """
UPDATE tickets
SET
    status = 'em_atendimento',
    called_at = datetime('now', 'localtime')
WHERE id = ?;
"""

FINISH_TICKET = """
UPDATE tickets
SET
    status = 'finalizado',
    finished_at = datetime('now', 'localtime'),
    service_time_seconds =
        CAST(strftime('%s', datetime('now', 'localtime')) AS INTEGER)
        -
        CAST(strftime('%s', called_at) AS INTEGER)
WHERE id = ?
AND status='em_atendimento';
"""

SKIP_TICKET = """
UPDATE tickets
SET
    status = 'ausente',
    finished_at = datetime('now', 'localtime')
WHERE id = ?
AND status = 'em_atendimento';
"""

CANCEL_TICKET = """
UPDATE tickets
SET
    status = 'cancelado',
    finished_at = datetime('now', 'localtime')
WHERE
    ticket_code = ?
    AND status = 'aguardando';
"""

