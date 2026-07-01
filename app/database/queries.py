

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

GET_NEXT_PRIORITY = """
SELECT *
FROM tickets
WHERE ticket_type = 'P'
AND status = 'aguardando'
ORDER BY created_at
LIMIT 1;
"""

GET_NEXT_NORMAL = """
SELECT *
FROM tickets
WHERE ticket_type = 'N'
AND status = 'aguardando'
ORDER BY created_at
LIMIT 1;
"""

#---atualiza---

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

#mudanca de estado para atendimento

CALL_TICKET = """
UPDATE tickets
SET
    status = 'em_atendimento',
    called_at = CURRENT_TIMESTAMP
WHERE id = ?;
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