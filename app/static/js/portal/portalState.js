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

    showSuccessNotification,

    showErrorNotification,

    showWarningNotification,

    showInfoNotification

} from "./portalNotifications.js";

let lastTicketStatus = null;

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

            if (lastTicketStatus !== "em_atendimento") {

                showSuccessNotification(
                    "Sua senha foi chamada. Dirija-se ao atendimento."
                );

            }

            lastTicketStatus = "em_atendimento";

            return;


        case "ausente":

            showAbsentView(ticket);

            finishPortal(
                "Sua senha foi marcada como ausente. Procure um atendente.",
                "error"
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
                "Seu atendimento foi finalizado.",
                "info"
            );

            return;

        default:

            resetPortal();

    }

}

// ======================================
// Finaliza sessão
// ======================================

function finishPortal(
    message,
    type = "info"
) {

    stopAutoRefresh();

    clearTicketSession();

    if (type === "success") {

        showSuccessNotification(message);

        return;

    }

    if (type === "error") {

        showErrorNotification(message);

        return;

    }

    if (type === "warning") {

        showWarningNotification(message);

        return;

    }

    showInfoNotification(message);

}

// ======================================
// Retorna tela inicial
// ======================================

function resetPortal() {

    stopAutoRefresh();

    clearTicketSession();

    lastTicketStatus = null;

    showHomeView();

}

