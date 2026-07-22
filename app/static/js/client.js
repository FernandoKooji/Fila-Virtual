// ==========================================
// Elementos da página
// ==========================================

const homeScreen = document.getElementById("home-screen");

const ticketScreen = document.getElementById("ticket-screen");

const btnEnter = document.getElementById("btn-enter");

const btnCancel = document.getElementById("btn-cancel");

const modal = document.getElementById("ticket-modal");

const btnConfirm = document.getElementById("btn-confirm");

const btnCloseModal = document.getElementById("btn-close-modal");

const ticketCodeText = document.getElementById("ticket-code");

const ticketStatusText = document.getElementById("ticket-status");

const ticketPositionText = document.getElementById("ticket-position");

const peopleAheadText = document.getElementById("people-ahead");


// ==========================================
// Variáveis globais
// ==========================================

let ticketCode = null;


// ==========================================
// Interface
// ==========================================

function showHome() {

    homeScreen.style.display = "block";

    ticketScreen.style.display = "none";

}

function showTicket() {

    homeScreen.style.display = "none";

    ticketScreen.style.display = "block";

}

function showModal() {

    modal.style.display = "flex";

}

function closeModal() {

    modal.style.display = "none";

}

async function checkLocalStorage() {

    ticketCode = localStorage.getItem(
        "ticket_code"
    );

    if (ticketCode) {

        ticketCodeText.textContent =
            ticketCode;

        showTicket();

        await loadTicketPosition();

    }

    else {

        showHome();

    }

}

// ==========================================
// API
// ==========================================

async function createTicket() {

    showModal();

}

async function confirmTicket() {

    const selectedType = document.querySelector(
        'input[name="ticket-type"]:checked'
    ).value;

    try {

        const response = await fetch("/tickets/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                ticket_type: selectedType
            })

        });
        
        //verifica se API responde correto
        if (!response.ok) {

            throw new Error("Erro ao criar a senha.");

        }
        
        const data = await response.json();

        console.log(data);

        if (data.success) {

            localStorage.setItem(
                "ticket_code",
                data.ticket_code
            );

            ticketCode = data.ticket_code;

            ticketCodeText.textContent = ticketCode;

            closeModal();

            showTicket();

            await loadTicketPosition();

        }

    }
    catch (error) {

        console.error(error);

    }

}

async function loadTicketPosition() {

    if (!ticketCode) {

        return;

    }

    try {

        const response = await fetch(

            `/queue/position/${ticketCode}`

        );

        if (!response.ok) {

            throw new Error(

                "Erro ao consultar posição."

            );

        }

        const data = await response.json();

        console.log(data);

        ticketStatusText.textContent =
            data.status;

        ticketPositionText.textContent =
            data.position + "º";

        peopleAheadText.textContent =
            data.people_ahead;

    }

    catch (error) {

        console.error(error);

    }

}

async function cancelTicket() {

    if (!ticketCode) {

        return;

    }

    const confirmed = confirm(

        "Deseja realmente cancelar sua senha?"

    );

    if (!confirmed) {

        return;

    }

    try {

        const response = await fetch(

            `/tickets/${ticketCode}`,

            {

                method: "DELETE"

            }

        );

        if (!response.ok) {

            throw new Error(

                "Erro ao cancelar senha."

            );

        }

        const data = await response.json();

        console.log(data);

        clearInterval(refreshInterval);

        localStorage.removeItem(

            "ticket_code"

        );

        ticketCode = null;

        showHome();

        startAutoRefresh();

    }

    catch(error){

        console.error(error);

    }

}

let refreshInterval = null;

function startAutoRefresh() {

    if (refreshInterval) {

        clearInterval(refreshInterval);

    }

    refreshInterval = setInterval(() => {

        if (ticketCode) {

            loadTicketPosition();

        }

    }, 5000);

}

// ==========================================
// Eventos
// ==========================================

btnEnter.addEventListener(
    "click",
    createTicket
);

btnConfirm.addEventListener(
    "click",
    confirmTicket
);

btnCloseModal.addEventListener(
    "click",
    closeModal
);

btnCancel.addEventListener(

    "click",

    cancelTicket

);

// ==========================================
// Inicialização
// ==========================================

checkLocalStorage();

startAutoRefresh();