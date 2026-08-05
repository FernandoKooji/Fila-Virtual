// ======================================
// Imports
// ======================================

import {

    showWaitingView,

    showCalledView,

    showAbsentView,

    showFinishedView,

    showCancelledView,

    showHomeView

} from "./portalView.js";

import {

    clearTicketSession,

    stopAutoRefresh

} from "./portalStorage.js";

import {

    showInfoNotification

} from "./portalNotifications.js";


// ======================================
// Atualiza estado do Portal
// ======================================

export function updatePortalState(ticket){

    if(!ticket){

        resetPortal();

        return;

    }

    switch(ticket.status){

        case "aguardando":

            showWaitingView(ticket);

            return;

        case "em_atendimento":

            showCalledView(ticket);

            showInfoNotification(

                "Sua senha foi chamada."

            );

            return;

        case "ausente":

            showAbsentView(ticket);

            finishPortal(

                "Sua senha foi marcada como ausente."

            );

            return;

        case "cancelado":

            showCancelledView(ticket);

            finishPortal(

                "Sua senha foi cancelada."

            );

            return;

        case "finalizado":

            showFinishedView(ticket);

            finishPortal(

                "Seu atendimento foi finalizado."

            );

            return;

        default:

            resetPortal();

    }

}

// ======================================
// Finaliza sessão
// ======================================

function finishPortal(message){

    // Para de consultar a API
    stopAutoRefresh();

    // Exibe a notificação mantendo a tela atual
    showInfoNotification(message);

    // Aguarda alguns segundos para o usuário ler
    setTimeout(() => {

        // Limpa a sessão
        clearTicketSession();

        // Volta para a tela inicial
        showHomeView();

    }, 5000);

}

// ======================================
// Retorna tela inicial
// ======================================

function resetPortal(){

    stopAutoRefresh();

    clearTicketSession();

    showHomeView();

}

