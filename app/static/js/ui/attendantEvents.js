// ======================================
// Imports
// ======================================

import {
    callNext,
    finishTicket,
    skipTicket,
    recallTicket
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

        await finishTicket();

        await refreshScreen();

    } catch (error) {

        console.error(error);

        showError(error.message);

    }

}

// ======================================
// Marcar senha como ausente
// ======================================

async function onSkipTicket() {

    try {

        await skipTicket();

        await refreshScreen();

    } catch (error) {

        console.error(error);

        showError(error.message);

    }

}

// ======================================
// Rechamar senha
// ======================================

async function onRecallTicket() {

    try {

        await recallTicket();

        /*
            Futuramente:

            - tocar campainha

            - enviar websocket

            - falar a senha (TTS)

            - atualizar TV
        */

    } catch (error) {

        console.error(error);

        showError(error.message);

    }

}

// ======================================
// Atualizar interface
// ======================================

async function refreshScreen() {

    await loadCurrentTicket();

    await loadQueue();

}

