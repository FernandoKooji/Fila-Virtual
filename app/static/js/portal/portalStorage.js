// ======================================
// Portal Storage
// ======================================

/*
    Gerencia a sessão do cliente
    armazenada no navegador.
*/

// ======================================
// Chaves do LocalStorage
// ======================================

const STORAGE_KEY = "ticketSession";

// ======================================
// Variáveis privadas
// ======================================

let autoRefreshId = null;

// ======================================
// Salvar sessão
// ======================================

export function saveTicketSession(ticket) {

    localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify(ticket)
    );

}

// ======================================
// Recuperar sessão
// ======================================

export function getTicketSession() {

    const data = localStorage.getItem(STORAGE_KEY);

    if (!data) {
        return null;
    }

    return JSON.parse(data);

}

// ======================================
// Existe sessão?
// ======================================

export function hasTicketSession() {

    return getTicketSession() !== null;

}

// ======================================
// Limpar sessão
// ======================================

export function clearTicketSession() {

    stopAutoRefresh();

    localStorage.removeItem(STORAGE_KEY);

}

// ======================================
// Iniciar atualização automática
// ======================================

export function startAutoRefresh(callback, interval = 5000) {

    stopAutoRefresh();

    autoRefreshId = setInterval(
        callback,
        interval
    );

}

// ======================================
// Parar atualização automática
// ======================================

export function stopAutoRefresh() {

    if (autoRefreshId !== null) {

        clearInterval(autoRefreshId);

        autoRefreshId = null;

    }

}

// ======================================
// Verifica se o polling está ativo
// ======================================

export function isAutoRefreshRunning() {

    return autoRefreshId !== null;

}