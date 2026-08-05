// ======================================
// Imports
// ======================================

import {

    createTicket,

    getTicketPosition,

    cancelTicket

} from "./portalApi.js";

import {

    saveTicketSession,

    getTicketSession,

    hasTicketSession,

    clearTicketSession,

    startAutoRefresh,

    stopAutoRefresh

} from "./portalStorage.js";

import {

    updatePortalState

} from "./portalState.js";

import {

    showHomeView

} from "./portalView.js";

import {

    showSuccessNotification,

    showErrorNotification,

    showInfoNotification,

    showConfirmNotification

} from "./portalNotifications.js";


// ======================================
// Elementos
// ======================================

import {

    btnEnter,

    btnCancel,

    btnConfirm,

    btnCloseModal,

    ticketModal

} from "./portalElements.js";


// ======================================
// Inicialização
// ======================================

export function registerPortalEvents(){

    registerButtons();

    restoreSession();

}

function registerButtons(){

    btnEnter?.addEventListener(

        "click",

        openModal

    );

    btnConfirm?.addEventListener(

        "click",

        confirmTicket

    );

    btnCloseModal?.addEventListener(

        "click",

        closeModal

    );

    btnCancel?.addEventListener(

        "click",

        handleCancel

    );

}

function openModal(){

    ticketModal.style.display = "flex";

}

function closeModal(){

    ticketModal.style.display = "none";

}

async function confirmTicket(){

    const type = document.querySelector(

        'input[name="ticket-type"]:checked'

    ).value;

    try{

        const ticket = await createTicket(type);

        saveTicketSession({

            ticketCode: ticket.ticket_code,

            ticketType: ticket.ticket_type

        });

        closeModal();

        await refreshTicket();

        startPolling();

        showSuccessNotification(

            "Senha criada com sucesso."

        );

    }

    catch(error){

        showErrorNotification(

            error.message

        );

    }

}

async function restoreSession(){

    if(!hasTicketSession()){

        showHomeView();

        return;

    }

    await refreshTicket();

    startPolling();

}

async function refreshTicket(){

    try{

        const ticket = getTicketSession();

        const response = await getTicketPosition(

            ticket.ticketCode

        );

        updatePortalState(

            response

        );

    }

    catch(error){

    console.error(error);

    }

}

function startPolling(){

    startAutoRefresh(

        refreshTicket,

        5000

    );

}

async function handleCancel(){

    const confirmed = await showConfirmNotification(

        "Cancelar senha?"

    );

    if(!confirmed){

        return;

    }

    try{

        const ticket = getTicketSession();

        await cancelTicket(

            ticket.ticketCode

        );

        clearPortal();

        showInfoNotification(

            "Senha cancelada."

        );

    }

    catch(error){

        showErrorNotification(

            error.message

        );

    }

}

function clearPortal(){

    stopAutoRefresh();

    clearTicketSession();

    showHomeView();

}

