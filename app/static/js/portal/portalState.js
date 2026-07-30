// ======================================
// Imports
// ======================================

import {

    clearTicketSession,

    stopAutoRefresh

} from "./portalStorage.js";

import {

    showCalledNotification,

    showAbsentNotification,

    showFinishedNotification,

    showCancelledNotification

} from "./portalNotifications.js";

import {

    showWaitingView,

    showCalledView,

    showHomeView

} from "./portalView.js";

// ======================================
// Atualiza estado do portal
// ======================================

export function updatePortalState(ticket){

    switch(ticket.status){

        case "aguardando":

            handleWaiting(ticket);

            break;

        case "em_atendimento":

            handleCalled(ticket);

            break;

        case "ausente":

            handleAbsent(ticket);

            break;

        case "cancelado":

            handleCancelled(ticket);

            break;

        case "finalizado":

            handleFinished(ticket);

            break;

        default:

            handleUnknown();

    }

}

function handleCalled(ticket){

    stopAutoRefresh();

    showCalledView(ticket);

    showCalledNotification();

}

function handleAbsent(){

    stopAutoRefresh();

    clearTicketSession();

    showAbsentView(ticket);

    showAbsentNotification(

        () => {

            showHomeView();

        }

    );

}

function handleCancelled(ticket){

    stopAutoRefresh();

    clearTicketSession();

    showCancelledView(ticket);

    showCancelledNotification(

    () => {

        showHomeView();

    }

);

}

function handleFinished(){

    stopAutoRefresh();

    clearTicketSession();

    showFinishedView(ticket);

    showFinishedNotification(

        () => {

            showHomeView();

        }

    );

}

function handleUnknown(){

    stopAutoRefresh();

    clearTicketSession();

    showHomeView();

}