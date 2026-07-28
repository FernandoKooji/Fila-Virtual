import {

    post,

    del,

    get

} from "./httpClient.js";

import {

    mapCreatedTicket,

    mapCanceledTicket,

    mapTicketPosition

} from "../mappers/ticketMapper.js";

const BASE_URL = "/tickets";


export async function createTicket(type) {

    const response = await post(

        BASE_URL,

        {

            ticket_type: type

        }

    );

    return mapCreatedTicket(

        response

    );

}


export async function cancelTicket(ticketCode) {

    const response = await del(

        `${BASE_URL}/${ticketCode}`

    );

    return mapCanceledTicket(

        response

    );

}


export async function getTicketPosition(ticketCode) {

    const response = await get(

        `${BASE_URL}/position/${ticketCode}`

    );

    return mapTicketPosition(

        response

    );

}