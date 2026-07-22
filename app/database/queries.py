#===SQL REUTILIZAVEIS===

#---criacao de senhas---
GET_LAST_PRIORITY = """
SELECT last_priority_number
FROM system_state
WHERE id = 1;
"""

GET_LAST_NORMAL = """
SELECT last_normal_number
FROM system_state
WHERE id = 1;
"""

#---procurar proxima senha e mudanca de estado para aguardando---
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
# Atualizacao
# ============================

#o contador das senhas
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

#estado: em atendimento
CALL_TICKET = """
UPDATE tickets
SET
    status = 'em_atendimento',
    called_at = CURRENT_TIMESTAMP
WHERE id = ?;
"""

#estado: atendimento finalizado
FINISH_TICKET = """
UPDATE tickets
SET
    status = 'finalizado',
    finished_at = CURRENT_TIMESTAMP,
    service_time_seconds =
        CAST(strftime('%s', CURRENT_TIMESTAMP) AS INTEGER)
        -
        CAST(strftime('%s', called_at) AS INTEGER)
WHERE id = ?
AND status='em_atendimento';
"""

#estado: ausente
SKIP_TICKET = """
UPDATE tickets
SET
    status = 'ausente',
    finished_at = CURRENT_TIMESTAMP
WHERE id = ?
AND status = 'em_atendimento';
"""

#cancelar uma senha
CANCEL_TICKET = """
UPDATE tickets
SET
    status = 'cancelado',
    finished_at = CURRENT_TIMESTAMP
WHERE
    id = ?
    AND status = 'aguardando';
"""

#---consulta de INSERT---
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
    CURRENT_TIMESTAMP
);
"""

# ============================
# Consulta posicao de senha (CLIENTE)
# ============================

# Busca dados da senha informada
GET_TICKET_POSITION = """
SELECT
    id,
    ticket_code,
    ticket_type,
    status,
    created_at
FROM tickets
WHERE ticket_code = ?;
"""

# Devolve senhas aguardando
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

# Buscar senha em atendimento
GET_CURRENT_TICKET_CODE = """
SELECT ticket_code
FROM tickets
WHERE status = 'em_atendimento'
LIMIT 1;
"""

# Cancelar senha
CANCEL_TICKET = """
UPDATE tickets
SET
    status = 'cancelado',
    finished_at = CURRENT_TIMESTAMP
WHERE
    ticket_code = ?
    AND status = 'aguardando';
"""