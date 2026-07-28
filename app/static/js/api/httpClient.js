// ======================================
// HTTP Client
// ======================================

/*
    Camada responsável por toda
    comunicação HTTP da aplicação.

    Nenhum outro arquivo deve utilizar
    fetch() diretamente.
*/

// ======================================
// Configuração
// ======================================

const DEFAULT_HEADERS = {

    "Content-Type": "application/json"

};

// ======================================
// Requisição genérica
// ======================================

async function request(
    url,
    options = {}
) {

    const response = await fetch(
        url,
        {

            headers: DEFAULT_HEADERS,

            ...options

        }
    );

    let data = null;

    try {

        data = await response.json();

    }

    catch {

        data = null;

    }

    if (!response.ok) {

        throw new Error(

            data?.detail ||

            data?.message ||

            "Erro na comunicação com o servidor."

        );

    }

    return data;

}

// ======================================
// GET
// ======================================

export async function get(url) {

    return request(
        url,
        {

            method: "GET"

        }
    );

}

// ======================================
// POST
// ======================================

export async function post(
    url,
    body = {}
) {

    return request(
        url,
        {

            method: "POST",

            body: JSON.stringify(body)

        }
    );

}

// ======================================
// PUT
// ======================================

export async function put(
    url,
    body = {}
) {

    return request(
        url,
        {

            method: "PUT",

            body: JSON.stringify(body)

        }
    );

}

// ======================================
// DELETE
// ======================================

export async function del(url) {

    return request(
        url,
        {

            method: "DELETE"

        }
    );

}

