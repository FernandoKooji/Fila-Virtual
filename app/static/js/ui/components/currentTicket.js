// ======================================
// Current Ticket Component
// ======================================

/*
    Responsável por renderizar
    a senha atualmente em atendimento.
*/


// ======================================
// Renderizar
// ======================================

export function renderCurrentTicket(ticket) {

    const container = document.getElementById(
        "currentTicket"
    );

    container.innerHTML = buildCurrentTicketHTML(
        ticket
    );

}


// ======================================
// Limpar
// ======================================

export function clearCurrentTicket() {

    const container = document.getElementById(
        "currentTicket"
    );

    container.innerHTML = `

        <p>

            Nenhuma senha em atendimento.

        </p>

    `;

}


// ======================================
// HTML
// ======================================

function buildCurrentTicketHTML(ticket) {

    return `

        <div class="current-ticket">

            <h1>

                ${ticket.ticketCode}

            </h1>

            <p>

                Tipo:
                ${ticket.ticketType}

            </p>

            <p>

                Status:
                ${ticket.status}

            </p>

            <p>

                Chamado às:

                ${ticket.calledAt}

            </p>

        </div>

    `;

}

