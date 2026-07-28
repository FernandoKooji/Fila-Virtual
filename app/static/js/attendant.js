import {
    loadCurrentTicket,
    loadQueue
} from "./ui/attendantView.js";

import {
    registerEvents
} from "./ui/attendantEvents.js";

function init(){

    loadCurrentTicket();

    loadQueue();

    registerEvents();

}

document.addEventListener(
    "DOMContentLoaded",
    init
);
