// ======================================
// Imports
// ======================================

import {

    get,

    post,

    del

} from "../api/httpClient.js";


// ======================================
// Criar senha
// ======================================

export async function createTicket(ticketType){

    return await post(

        "/tickets/",

        {

            ticket_type: ticketType

        }

    );

}


// ======================================
// Consultar posição
// ======================================

export async function getTicketPosition(ticketCode){

    return await get(

        `/queue/position/${ticketCode}`

    );

}


// ======================================
// Cancelar senha
// ======================================

export async function cancelTicket(ticketCode){

    return await del(

        `/tickets/${ticketCode}`

    );

}


// ======================================
// Status da fila
// ======================================

export async function getQueueStatus(){

    return await get(

        "/queue/status"

    );

}


// ======================================
// Atendimento atual
// ======================================

export async function getCurrentTicket(){

    return await get(

        "/queue/current"

    );

}