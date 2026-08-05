// ======================================
// Portal View
// ======================================

/*
    Responsável por atualizar
    toda a interface do Portal.
*/

// ======================================
// Elementos
// ======================================

import {

    homeSection,

    ticketSection,

    ticketCard

} from "./portalElements.js";


// ======================================
// Tela inicial
// ======================================

export function showHomeView(){

    homeSection.hidden = false;

    ticketSection.hidden = true;

}


// ======================================
// Tela aguardando
// ======================================

export function showWaitingView(ticket){

    showTicketSection();

    renderTicketCard({

        ticketCode: ticket.ticket_code,

        title: "Aguardando atendimento",

        message: "Aguarde sua chamada.",

        statusClass: "waiting",

        position: ticket.position,

        peopleAhead: ticket.people_ahead

    });

}


// ======================================
// Tela senha chamada
// ======================================

export function showCalledView(ticket){

    showTicketSection();

    renderTicketCard({

        ticketCode: ticket.ticket_code,

        title: "Sua senha foi chamada",

        message: "Dirija-se ao atendimento.",

        statusClass: "success"

    });

}


// ======================================
// Tela ausente
// ======================================

export function showAbsentView(ticket){

    showTicketSection();

    renderTicketCard({

        ticketCode: ticket.ticket_code,

        title: "Senha marcada como ausente",

        message: "Procure um atendente.",

        statusClass: "danger"

    });

}


// ======================================
// Tela atendimento finalizado
// ======================================

export function showFinishedView(ticket){

    showTicketSection();

    renderTicketCard({

        ticketCode: ticket.ticket_code,

        title: "Atendimento finalizado",

        message: "Obrigado pela preferência. Você pode fechar o portal",

        statusClass: "info"

    });

}


// ======================================
// Tela cancelada
// ======================================

export function showCancelledView(ticket){

    showTicketSection();

    renderTicketCard({

        ticketCode: ticket.ticket_code,

        title: "Senha cancelada",

        message: "Você saiu da fila.",

        statusClass: "warning"

    });

}


// ======================================
// Exibe tela da senha
// ======================================

function showTicketSection(){

    homeSection.hidden = true;

    ticketSection.hidden = false;

}


// ======================================
// Renderização única
// ======================================

function renderTicketCard(data){

    ticketCard.innerHTML = `

        <div class="ticket-card ${data.statusClass}">

            <h1>

                ${data.ticketCode}

            </h1>

            <h2>

                ${data.title}

            </h2>

            <p>

                ${data.message}

            </p>

            ${renderQueueInfo(data)}

        </div>

    `;

}


// ======================================
// Informações da fila
// ======================================

function renderQueueInfo(data){

    if(data.position === undefined){

        return "";

    }

    return `

        <hr>

        <p>

            <strong>Posição:</strong>

            ${data.position}

        </p>

        <p>

            <strong>Pessoas à frente:</strong>

            ${data.peopleAhead}

        </p>

    `;

}