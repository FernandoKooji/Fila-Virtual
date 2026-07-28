// ======================================
// Imports
// ======================================

import {

    get,

    post

} from "./httpClient.js";

import {

    mapQueue,

    mapQueueStatus

} from "../mappers/queueMapper.js";

import {

    mapCurrentTicket

} from "../mappers/ticketMapper.js";

// ======================================
// Base URL
// ======================================

const BASE_URL = "/queue";

// ======================================
// Atendimento atual
// ======================================

export async function getCurrentTicket() {

    const response = await get(

        `${BASE_URL}/current`

    );

    return mapCurrentTicket(

        response

    );

}
// ======================================
// Lista da fila
// ======================================

export async function getQueueList() {

    const response = await get(

        `${BASE_URL}/list`

    );

    return mapQueue(

        response

    );

}

// ======================================
// Chamar próxima
// ======================================

export async function callNext() {

    return post(

        `${BASE_URL}/next`

    );

}

// ======================================
// Rechamar senha
// ======================================

export async function recallTicket() {

    return post(

        `${BASE_URL}/recall`

    );

}

// ======================================
// Finalizar atendimento
// ======================================

export async function finishTicket(id) {

    return post(

        `${BASE_URL}/finish`,

        {

            id

        }

    );

}

// ======================================
// Marcar como ausente
// ======================================

export async function skipTicket(id) {

    return post(

        `${BASE_URL}/skip`,

        {

            id

        }

    );

}

// ======================================
// Status da fila
// ======================================

export async function getQueueStatus() {

    const response = await get(

        `${BASE_URL}/status`

    );

    return mapQueueStatus(

        response

    );

}
