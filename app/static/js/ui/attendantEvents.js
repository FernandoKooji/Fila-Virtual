// ======================================
// Imports
// ======================================

import {
    callNext,
    finishTicket,
    skipTicket,
    recallTicket,
    getCurrentTicket
} from "../api/queueApi.js";

import {
    loadCurrentTicket,
    loadQueue
} from "./attendantView.js";

import {
    showError
} from "./notifications.js";

// ======================================
// Registrar eventos
// ======================================

export function registerEvents() {

    document
        .getElementById("btnNext")
        ?.addEventListener(
            "click",
            onCallNext
        );

    document
        .getElementById("btnFinish")
        ?.addEventListener(
            "click",
            onFinishTicket
        );

    document
        .getElementById("btnSkip")
        ?.addEventListener(
            "click",
            onSkipTicket
        );

    document
        .getElementById("btnRecall")
        ?.addEventListener(
            "click",
            onRecallTicket
        );
}

// ======================================
// Funções auxiliares
// ======================================

async function getCurrentTicketId() {

    const ticket = await getCurrentTicket();

    if (!ticket?.id) {

        throw new Error(
            "Nenhuma senha em atendimento."
        );

    }

    return ticket.id;

}

// ======================================
// Atualizar interface
// ======================================

async function refreshScreen() {

    await Promise.all([

        loadCurrentTicket(),

        loadQueue()

    ]);

}

// ======================================
// Chamar próxima senha
// ======================================

async function onCallNext() {

    try {

        await callNext();

        await refreshScreen();

    } catch (error) {

    console.error(error);

    showError(error.message);

    }

}

// ======================================
// Finalizar atendimento
// ======================================

async function onFinishTicket() {

    try {

        const ticketId = await getCurrentTicketId();

        await finishTicket(
            ticketId
        );

        await refreshScreen();

    }

    catch (error) {

        console.error(error);

        showError(error.message);

    }

}

/// ======================================
// Marcar senha como ausente
// ======================================

async function onSkipTicket() {

    try {

        const ticketId = await getCurrentTicketId();

        await skipTicket(
            ticketId
        );

        await refreshScreen();

    }

    catch (error) {

        console.error(error);

        showError(error.message);

    }

}

// ======================================
// Rechamar senha
// ======================================

async function onRecallTicket() {

    try {

        const ticketId = await getCurrentTicketId();

        await recallTicket(
            ticketId
        );

    }

    catch (error) {

        console.error(error);

        showError(error.message);

    }

}

