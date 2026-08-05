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

const BASE_URL = "";


// ======================================
// GET
// ======================================

export async function get(url){

    const response = await fetch(

        BASE_URL + url

    );

    return await parseResponse(response);

}


// ======================================
// POST
// ======================================

export async function post(url, body){

    const response = await fetch(

        BASE_URL + url,

        {

            method: "POST",

            headers: {

                "Content-Type":"application/json"

            },

            body: JSON.stringify(body)

        }

    );

    return await parseResponse(response);

}


// ======================================
// DELETE
// ======================================

export async function del(url){

    const response = await fetch(

        BASE_URL + url,

        {

            method:"DELETE"

        }

    );

    return await parseResponse(response);

}


// ======================================
// Tratamento
// ======================================

async function parseResponse(response){

    const data = await response.json();

    if(!response.ok){

        throw new Error(

            data.detail ||

            "Erro inesperado."

        );

    }

    return data;

}