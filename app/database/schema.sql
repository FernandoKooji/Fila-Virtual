/*==TABELAS==*/

--CREATE TABLE IF NOT EXISTS--

--senhas geradas

CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    ticket_code TEXT NOT NULL,

    ticket_type CHAR(1) NOT NULL,

    status TEXT NOT NULL,

    created_at DATETIME NOT NULL,

    called_at DATETIME,

    finished_at DATETIME,

    wait_time_seconds INTEGER,

    service_time_seconds INTEGER
);

--estado do sistema--

CREATE TABLE IF NOT EXISTS system_state (
    id INTEGER PRIMARY KEY,

    last_normal_number INTEGER NOT NULL,

    last_priority_number INTEGER NOT NULL
);

/*==REGRAS DA FILA e tipos de senha==*/

--Inicializar sistema--

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

--senha normal--

SELECT last_normal_number
FROM system_state
WHERE id = 1;

--senha preferencial--

SELECT last_priority_number
FROM system_state
WHERE id = 1;