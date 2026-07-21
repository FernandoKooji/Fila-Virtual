// =========================
// Elementos
// =========================

const homeScreen =
    document.getElementById("home-screen");

const ticketScreen =
    document.getElementById("ticket-screen");

const btnEnter =
    document.getElementById("btn-enter");

const btnCancel =
    document.getElementById("btn-cancel");

const modal =
    document.getElementById("ticket-modal");

const btnConfirm =
    document.getElementById("btn-confirm");

const btnCloseModal =
    document.getElementById("btn-close-modal");

// =========================
// Variáveis
// =========================

let ticketCode = null;


// =========================
// Interface
// =========================

function showHome(){

    homeScreen.style.display = "block";

    ticketScreen.style.display = "none";

}

function showTicket(){

    homeScreen.style.display = "none";

    ticketScreen.style.display = "block";

}

function showModal() {

    modal.style.display = "flex";

}

function closeModal() {

    modal.style.display = "none";

}

function checkLocalStorage(){

    ticketCode = localStorage.getItem("ticket_code");

    if(ticketCode){

        showTicket();

    }else{

        showHome();

    }

}


// =========================
// API
// =========================

async function createTicket(){

    showModal();

}

async function confirmTicket(){

    const selectedType = document.querySelector(

        'input[name="ticket-type"]:checked'

    ).value;

    console.log(

        "Tipo selecionado:",

        selectedType

    );

    closeModal();

}

// =========================
// Eventos
// =========================

btnEnter.addEventListener(

    "click",

    createTicket

);

btnCloseModal.addEventListener(

    "click",

    closeModal

);

btnConfirm.addEventListener(

    "click",

    confirmTicket

);


// =========================
// Inicialização
// =========================

checkLocalStorage();