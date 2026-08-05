import {
    loadCurrentTicket,
    loadQueue,
    refreshView
} from "./ui/attendantView.js";

import {
    registerEvents
} from "./ui/attendantEvents.js";

let refreshInterval;

function startAutoRefresh(){

    refreshInterval = setInterval(

        refreshView,

        3000

    );

}

function init(){

    loadCurrentTicket();

    loadQueue();

    registerEvents();

    startAutoRefresh();

}

document.addEventListener(
    "DOMContentLoaded",
    init
);
