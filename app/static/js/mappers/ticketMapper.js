// ======================================
// Ticket Mapper
// ======================================

/*
    Converte respostas da API
    relacionadas às senhas.
*/


// ======================================
// Criar senha
// ======================================

export function mapCreatedTicket(response) {

    return {

        id: response.id,

        ticketCode: response.ticket_code,

        ticketType: response.ticket_type,

        status: response.status

    };

}


// ======================================
// Cancelar senha
// ======================================

export function mapCanceledTicket(response) {

    return {

        success: response.success,

        message: response.message

    };

}


// ======================================
// Consulta de posição
// ======================================

export function mapTicketPosition(response) {

    return {

        ticketCode: response.ticket_code,

        status: response.status,

        position: response.position,

        peopleAhead: response.people_ahead

    };

}


// ======================================
// Ticket em atendimento
// ======================================

export function mapCurrentTicket(response) {

    return {

        id: response.id,

        ticketCode: response.ticket_code,

        ticketType: response.ticket_type,

        status: response.status,

        calledAt: response.called_at

    };

}