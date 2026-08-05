// ======================================
// Portal Storage
// ======================================

/*
    Responsável por:

    - LocalStorage
    - Sessão da senha
    - Atualização automática
*/

// ======================================
// Chaves
// ======================================

const STORAGE_KEY = "ticketSession";


// ======================================
// Polling
// ======================================

let refreshInterval = null;


// ======================================
// Sessão
// ======================================

export function saveTicketSession(ticket){

    localStorage.setItem(

        STORAGE_KEY,

        JSON.stringify(ticket)

    );

}


export function getTicketSession(){

    const data = localStorage.getItem(

        STORAGE_KEY

    );

    if(!data){

        return null;

    }

    return JSON.parse(data);

}


export function hasTicketSession(){

    return getTicketSession() !== null;

}


export function clearTicketSession(){

    localStorage.removeItem(

        STORAGE_KEY

    );

}


// ======================================
// Atualização automática
// ======================================

export function startAutoRefresh(callback, interval = 5000){

    stopAutoRefresh();

    refreshInterval = setInterval(

        callback,

        interval

    );

}


export function stopAutoRefresh(){

    if(refreshInterval){

        clearInterval(refreshInterval);

        refreshInterval = null;

    }

}