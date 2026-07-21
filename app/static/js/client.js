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

    console.log("Criar senha");

}


// =========================
// Eventos
// =========================

btnEnter.addEventListener(

    "click",

    createTicket

);


// =========================
// Inicialização
// =========================

checkLocalStorage();