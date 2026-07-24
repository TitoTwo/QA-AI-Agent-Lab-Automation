import { useState } from "react";
import { useScrollToTop } from "../../hooks/useScrollToTop";

import {
    simularFinanciacion,
    confirmarFinanciacion
} from "../../api/bancoApi";

import Paso1 from "./Paso1";
import Paso2 from "./Paso2";
import Paso3 from "./Paso3";
import ThankYouPage from "./ThankYouPage";

function FinanciarSaldo({ tarjeta, volver }) {

    useScrollToTop();

    const [paso, setPaso] = useState(1);

    const [montoSeleccionado, setMontoSeleccionado] = useState(null);

    const [cuotasSeleccionadas, setCuotasSeleccionadas] = useState(null);

    const [simulacion, setSimulacion] = useState(null);

    const [operacion, setOperacion] = useState(null);

    return (

        <>

            {paso === 1 && (

                <Paso1

                    tarjeta={tarjeta}

                    volver={volver}

                    continuar={(monto) => {

                        setMontoSeleccionado(monto);

                        setPaso(2);

                    }}

                />

            )}

            {paso === 2 && (

                <Paso2

                    tarjeta={tarjeta}

                    monto={montoSeleccionado}

                    volver={() => setPaso(1)}

                    continuar={async (cuotas) => {

                        try {

                            const resultado = await simularFinanciacion(

                                montoSeleccionado,

                                cuotas

                            );

                            setCuotasSeleccionadas(cuotas);

                            setSimulacion(resultado);

                            setPaso(3);

                        }

                        catch (error) {

                            console.error(error);

                            alert("No fue posible calcular la financiación.");

                        }

                    }}

                />

            )}

            {paso === 3 && (

                <Paso3

                    tarjeta={tarjeta}

                    simulacion={simulacion}

                    volver={() => setPaso(2)}

                    confirmar={async () => {

                    try {

                        const resultado = await confirmarFinanciacion(

                            simulacion.monto,

                            simulacion.cuotas

                        );

                        setOperacion(resultado);

                        setPaso(4);

                    } catch (error) {

                        console.error(error);

                        alert("No fue posible confirmar la financiación.");

                    }

                }}

                />

            )}

            {paso === 4 && (

                <ThankYouPage

                    tarjeta={tarjeta}

                    operacion={operacion}

                    volver={volver}

                />

            )}

        </>

    );

}

export default FinanciarSaldo;