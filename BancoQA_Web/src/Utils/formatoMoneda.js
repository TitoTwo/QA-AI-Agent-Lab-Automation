export function formatoMoneda(valor, moneda){


    const numero = valor.toLocaleString(
        "es-AR"
    );


    switch(moneda){


        case "USD":

            return `U$S ${numero}`;


        case "EUR":

            return `€ ${numero}`;


        case "ARS":

        default:

            return `$ ${numero}`;

    }

}