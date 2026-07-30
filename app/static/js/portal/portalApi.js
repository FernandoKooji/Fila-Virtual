// ======================================
// Imports
// ======================================

import {

    get,

    post

} from "../api/httpClient.js";

// ======================================
// Endpoints
// ======================================

const QUEUE_URL = "/queue";

const TICKET_URL = "/tickets";

// ======================================
// Consulta posição
// ======================================

export async function getTicketPosition(ticketCode){

    return await get(

        `${QUEUE_URL}/position/${ticketCode}`

    );

}

// ======================================
// Cancelar senha
// ======================================

export async function cancelTicket(ticketCode){

    return await post(

        `${TICKET_URL}/cancel`,

        {

            ticket_code: ticketCode

        }

    );

}

// ======================================
// Consulta status da fila
// ======================================

export async function getQueueStatus(){

    return await get(

        `${QUEUE_URL}/status`

    );

}

// ======================================
// Atendimento atual
// ======================================

export async function getCurrentTicket(){

    return await get(

        `${QUEUE_URL}/current`

    );

}

