// ======================================
// Portal Notifications
// ======================================

/*
    Todas as mensagens do Portal
    passam por este arquivo.
*/

function showNotification(title, message){

    alert(

        `${title}\n\n${message}`

    );

}

export function showCalledNotification(callback){

    showNotification(

        "Sua senha foi chamada",

        "Dirija-se ao atendimento.",

        callback

    );

}

export function showAbsentNotification(callback){

    showNotification(

        "Senha marcada como ausente",

        "Procure um atendente para obter orientações.",

        callback

    );

}

export function showFinishedNotification(callback){

    showNotification(

        "Atendimento finalizado",

        "Obrigado por utilizar nosso atendimento.",

        callback

    );

}

export function showCancelledNotification(callback){

    showNotification(

        "Senha cancelada",

        "Sua senha foi removida da fila.",

        callback

    );

}

export function showErrorNotification(message){

    showNotification(

        "Erro",

        message

    );

}

export function showInfoNotification(message){

    alert(message);

}

export function showSuccessNotification(message){

    showNotification(

        "Sucesso",

        message

    );

}

export function showConfirmNotification(message){

    return confirm(message);

}