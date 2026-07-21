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

function checkLocalStorage() {

    ticketCode = localStorage.getItem("ticket_code");

    if (ticketCode) {

        ticketCodeText.textContent = ticketCode;

        showTicket();

    } else {

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

        }

    }
    catch (error) {

        console.error(error);

    }

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


// ==========================================
// Inicialização
// ==========================================

checkLocalStorage();