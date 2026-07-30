// ======================================
// Imports
// ======================================

import {

    getTicketSession,

    hasTicketSession,

    clearTicketSession,

    startAutoRefresh,

    stopAutoRefresh

} from "./portalStorage.js";

import {

    getTicketPosition,

    cancelTicket

} from "./portalApi.js";

import {

    updatePortalState

} from "./portalState.js";

import {

    showErrorNotification

} from "./portalNotifications.js";


// ======================================
// Registrar eventos
// ======================================

export function registerPortalEvents(){

    registerCancelButton();

    restorePortalSession();

}

// ======================================
// Botão cancelar senha
// ======================================

function registerCancelButton(){

    const button = document.getElementById("cancelTicketButton");

    if(!button){

        return;

    }

    button.addEventListener(

        "click",

        handleCancelTicket

    );

}

async function handleCancelTicket(){

    const ticket = getTicketSession();

    if(!ticket){

        return;

    }

    try{

        await cancelTicket(

            ticket.ticketCode

        );

        clearTicketSession();

        location.reload();

    }

    catch(error){

        showErrorNotification(

            error.message

        );

    }

}

// ======================================
// Restaurar sessão
// ======================================

async function restorePortalSession(){

    if(

        !hasTicketSession()

    ){

        return;

    }

    const ticket = getTicketSession();

    await updateTicketStatus(

        ticket.ticketCode

    );

    startPolling(

        ticket.ticketCode

    );

}

async function updateTicketStatus(ticketCode){

    try{

        const response =

            await getTicketPosition(

                ticketCode

            );

        updatePortalState(

            response

        );

    }

    catch(error){

        showErrorNotification(

            error.message

        );

    }

}

function startPolling(ticketCode){

    startAutoRefresh(

        async ()=>{

            await updateTicketStatus(

                ticketCode

            );

        },

        5000

    );

}

export function stopPortalPolling(){

    stopAutoRefresh();

}