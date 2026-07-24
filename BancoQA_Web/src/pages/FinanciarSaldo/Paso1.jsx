import { useMemo, useState } from "react";
import { useScrollToTop } from "../../hooks/useScrollToTop";

import Header from "../../components/Header/Header";

import BackButton from "../../components/common/BackButton";
import PrimaryButton from "../../components/common/PrimaryButton";
import Card from "../../components/common/Card";
import StepIndicator from "../../components/common/StepIndicator";

import { formatoMoneda } from "../../utils/formatoMoneda";

import "./FinanciarSaldo.css";
import "./Paso1.css";

function Paso1({

    tarjeta,

    volver,

    continuar

}) {

    useScrollToTop();

    const MONTO_MINIMO = 100;

    const montoMaximo = tarjeta.saldo_pesos ?? 0;

    const [tipoMonto, setTipoMonto] = useState("MAXIMO");

    const [otroImporte, setOtroImporte] = useState("");

    const importeElegido = useMemo(() => {

        if (tipoMonto === "MAXIMO") {

            return montoMaximo;

        }

        return Number(otroImporte);

    }, [tipoMonto, otroImporte, montoMaximo]);

    const mensajeError = useMemo(() => {

        if (tipoMonto === "MAXIMO") return "";

        if (otroImporte === "") return "";

        if (Number(otroImporte) < MONTO_MINIMO) {

            return `El importe mínimo para financiar es de ${formatoMoneda(MONTO_MINIMO, "ARS")}`;

        }

        if (Number(otroImporte) > montoMaximo) {

            return "El importe supera el máximo financiable.";

        }

        return "";

    }, [tipoMonto, otroImporte, montoMaximo]);

    const puedeContinuar = useMemo(() => {

        if (tipoMonto === "MAXIMO") {

            return montoMaximo >= MONTO_MINIMO;

        }

        return (

            Number(otroImporte) >= MONTO_MINIMO &&

            Number(otroImporte) <= montoMaximo

        );

    }, [tipoMonto, otroImporte, montoMaximo]);

    return (

        <div className="home-container">

            <Header
                mostrarBanner={false}
                titulo="Financiación de saldos"
                mostrarCerrar={true}
                cerrar={volver}
            />

            <div className="financiar-container">

                <StepIndicator
                    paso={1}
                    total={4}
                    className="paso-indicador"
                />

                <h2 className="financiar-titulo">

                    Financiación de saldos

                </h2>

                <Card className="tarjeta-box">

                    <div className="tarjeta-nombre">

                        {tarjeta.nombre}

                    </div>

                    <div className="tarjeta-numero">

                        {tarjeta.numero}

                    </div>

                </Card>

                <div className="financiar-bloque">

                    <h3>

                        Monto a financiar

                    </h3>

                    <label className="radio-item">

                        <input
                            type="radio"
                            checked={tipoMonto === "MAXIMO"}
                            onChange={() => setTipoMonto("MAXIMO")}
                        />

                        <span>

                            Máximo financiable

                        </span>

                    </label>

                    <div className="importe-maximo">

                        {formatoMoneda(montoMaximo, "ARS")}

                    </div>



                    <label className="radio-item radio-separador">

                        <input
                            type="radio"
                            checked={tipoMonto === "OTRO"}
                            onChange={() => setTipoMonto("OTRO")}
                        />

                        <span>

                            Otro importe

                        </span>



                    </label>


                    {

                        tipoMonto === "OTRO" && (

                            <div className="otro-importe-box">

                                <div className="input-pesos">

                                    <span className="simbolo-peso">

                                        $

                                    </span>

                                    <input
                                        className="input-importe"
                                        type="number"
                                        placeholder="Ingrese el importe"
                                        value={otroImporte}
                                        onChange={(e) => setOtroImporte(e.target.value)}
                                    />

                                </div>

                                <div className="texto-ayuda">

                                    Podés elegir financiar desde{" "}

                                    <strong>

                                        {formatoMoneda(MONTO_MINIMO, "ARS")}

                                    </strong>

                                    {" "}hasta el monto máximo disponible.

                                </div>

                                {

                                    mensajeError && (

                                        <div className="mensaje-error">

                                            {mensajeError}

                                        </div>

                                    )

                                }

                            </div>

                        )

                    }

                </div>

                <div className="financiar-footer">

                    <BackButton
                        onClick={volver}
                        className="btn-volver-financiacion"
                    />

                    <PrimaryButton
                        onClick={() => continuar(importeElegido)}
                        disabled={!puedeContinuar}
                        className="btn-continuar"
                    >

                        Continuar

                    </PrimaryButton>

                </div>

            </div>

        </div>

    );

}

export default Paso1;