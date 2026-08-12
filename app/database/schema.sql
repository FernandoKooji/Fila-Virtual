/*==TABELAS==*/

CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    ticket_code TEXT NOT NULL UNIQUE,

    ticket_type CHAR(1) NOT NULL,

    status TEXT NOT NULL,

    created_at DATETIME NOT NULL,

    called_at DATETIME,

    finished_at DATETIME,

    wait_time_seconds INTEGER,

    service_time_seconds INTEGER
);


CREATE TABLE IF NOT EXISTS system_state (
    id INTEGER PRIMARY KEY,

    last_normal_number INTEGER NOT NULL,

    last_priority_number INTEGER NOT NULL
);


/*==REGRAS DA FILA e tipos de senha==*/

INSERT OR IGNORE INTO system_state (
    id,
    last_normal_number,
    last_priority_number
)
VALUES (
    1,
    0,
    0
);


CREATE INDEX IF NOT EXISTS idx_ticket_status
ON tickets(status);


CREATE INDEX IF NOT EXISTS idx_ticket_created_at
ON tickets(created_at);