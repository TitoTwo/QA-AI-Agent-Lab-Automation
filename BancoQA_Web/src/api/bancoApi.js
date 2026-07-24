import axios from "axios";

const bancoApi = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

export async function simularFinanciacion(monto, cuotas) {

    const response = await bancoApi.post(
        "/financiacion/simular",
        {
            monto,
            cuotas
        }
    );

    return response.data;

}

export async function confirmarFinanciacion(monto, cuotas) {

    const response = await bancoApi.post(

        "/financiacion/confirmar",

        {
            monto,
            cuotas
        }

    );

    return response.data;

}

export default bancoApi;