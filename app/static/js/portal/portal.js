// ======================================
// Imports
// ======================================

import {

    registerPortalEvents

} from "./portalEvents.js";


// ======================================
// Inicialização
// ======================================

function init(){

    registerPortalEvents();

}


// ======================================
// Evento da página
// ======================================

document.addEventListener(

    "DOMContentLoaded",

    init

);

