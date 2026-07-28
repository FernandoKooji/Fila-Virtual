// ======================================
// Response Mapper
// ======================================

/*
    Padroniza respostas
    vindas do backend.
*/


// ======================================
// Sucesso
// ======================================

export function mapSuccess(response) {

    return {

        success: true,

        data: response

    };

}


// ======================================
// Erro
// ======================================

export function mapError(error) {

    return {

        success: false,

        message:

            error?.message ||

            "Erro inesperado."

    };

}