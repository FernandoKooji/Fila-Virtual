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

const ticketCard =
    document.getElementById("ticketCard");

const homeSection =
    document.getElementById("homeSection");

const ticketSection =
    document.getElementById("ticketSection");

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

    homeSection.hidden = true;

    ticketSection.hidden = false;

    ticketCard.innerHTML = waitingTemplate(ticket);

}

// ======================================
// Tela senha chamada
// ======================================

export function showCalledView(ticket){

    homeSection.hidden = true;

    ticketSection.hidden = false;

    ticketCard.innerHTML = calledTemplate(ticket);

}

// ======================================
// Tela ausente
// ======================================

export function showAbsentView(ticket){

    homeSection.hidden = true;

    ticketSection.hidden = false;

    ticketCard.innerHTML = absentTemplate(ticket);

}

// ======================================
// Tela atendimento finalizado
// ======================================

export function showFinishedView(ticket){

    homeSection.hidden = true;

    ticketSection.hidden = false;

    ticketCard.innerHTML = finishedTemplate(ticket);

}

// ======================================
// Tela cancelada
// ======================================

export function showCancelledView(ticket){

    homeSection.hidden = true;

    ticketSection.hidden = false;

    ticketCard.innerHTML = cancelledTemplate(ticket);

}

// ======================================
// Templates
// ======================================

function waitingTemplate(ticket){

    return `

        <div class="ticket-card">

            <h1>${ticket.ticket_code}</h1>

            <h2>Aguardando atendimento</h2>

            <p>

                Posição:
                <strong>${ticket.position}</strong>

            </p>

            <p>

                Pessoas à frente:
                <strong>${ticket.people_ahead}</strong>

            </p>

        </div>

    `;

}

function calledTemplate(ticket){

    return `

        <div class="ticket-card success">

            <h1>${ticket.ticket_code}</h1>

            <h2>Sua senha foi chamada</h2>

            <p>

                Dirija-se ao atendimento.

            </p>

        </div>

    `;

}

function absentTemplate(ticket){

    return `

        <div class="ticket-card danger">

            <h1>${ticket.ticket_code}</h1>

            <h2>Senha marcada como ausente</h2>

            <p>

                Procure um atendente.

            </p>

        </div>

    `;

}

function finishedTemplate(ticket){

    return `

        <div class="ticket-card info">

            <h1>${ticket.ticket_code}</h1>

            <h2>Atendimento finalizado</h2>

            <p>

                Obrigado pela preferência.

            </p>

        </div>

    `;

}

function cancelledTemplate(ticket){

    return `

        <div class="ticket-card warning">

            <h1>${ticket.ticket_code}</h1>

            <h2>Senha cancelada</h2>

            <p>

                Você saiu da fila.

            </p>

        </div>

    `;

}