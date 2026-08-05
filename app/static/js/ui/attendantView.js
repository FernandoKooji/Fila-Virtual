// ======================================
// Imports
// ======================================

import {

    getCurrentTicket,

    getQueueList

} from "../api/queueApi.js";

import {

    renderCurrentTicket,

    clearCurrentTicket

} from "./components/currentTicket.js";


// ======================================
// Carregar atendimento atual
// ======================================

export async function loadCurrentTicket() {

    try {

        const ticket = await getCurrentTicket();

        renderCurrentTicket(ticket);

    }

    catch {

        clearCurrentTicket();

    }

}


// ======================================
// Carregar fila
// ======================================

export async function loadQueue() {

    try {

        const queue = await getQueueList();

        renderQueue(queue);

    }

    catch {

        clearQueue();

    }

}


// ======================================
// Renderizar fila
// ======================================

export function renderQueue(queue) {

    const list = document.getElementById(
        "queueList"
    );

    list.innerHTML = buildQueueHTML(
        queue
    );

}


// ======================================
// Gerar HTML da fila
// ======================================

function buildQueueHTML(queue) {

    if (!queue || queue.length === 0) {

        return `

            <li>

                Nenhuma senha aguardando.

            </li>

        `;

    }

    return queue.map(

        ticket => `

            <li class="queue-item">

                <span class="queue-position">

                    ${ticket.position}º

                </span>

                <span class="queue-code">

                    ${ticket.ticket_code}

                </span>

                <span class="queue-type">

                    ${ticket.ticket_type}

                </span>

            </li>

        `

    ).join("");

}


// ======================================
// Limpar fila
// ======================================

export function clearQueue() {

    const list = document.getElementById(
        "queueList"
    );

    list.innerHTML = `

        <li>

            Nenhuma senha aguardando.

        </li>

    `;

}


// ======================================
// Atualizar toda a interface
// ======================================

export async function refreshView(){

    await loadCurrentTicket();

    await loadQueue();

}