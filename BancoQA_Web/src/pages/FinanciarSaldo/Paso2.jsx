import { useState } from "react";
import { useScrollToTop } from "../../hooks/useScrollToTop";

import Header from "../../components/Header/Header";

import BackButton from "../../components/common/BackButton";
import PrimaryButton from "../../components/common/PrimaryButton";
import StepIndicator from "../../components/common/StepIndicator";
import Card from "../../components/common/Card";
import Select from "../../components/common/Select";

import { formatoMoneda } from "../../utils/formatoMoneda";

import "./FinanciarSaldo.css";
import "./Paso2.css";

function Paso2({

    tarjeta,

    monto,

    volver,

    continuar,

    cerrar

}) {

    useScrollToTop();

    const [cuotaSeleccionada, setCuotaSeleccionada] = useState(3);

    const cuotas = [

        { value: 3, label: "3 cuotas" },

        { value: 6, label: "6 cuotas" },

        { value: 12, label: "12 cuotas" },

        { value: 18, label: "18 cuotas" },

        { value: 24, label: "24 cuotas" }

    ];

    const continuarPaso = () => {

        continuar(cuotaSeleccionada);

    };

    return (

        <div className="home-container">

            <Header
                mostrarBanner={false}
                titulo="Financiación de saldos"
                mostrarCerrar={true}
                cerrar={cerrar}
            />

            <div className="financiar-container">

                <StepIndicator
                    paso={2}
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

                    <div className="monto-financiar">

                        {formatoMoneda(monto, "ARS")}

                    </div>

                </div>

                <div className="financiar-bloque">

                    <h3>

                        Seleccioná la cantidad de cuotas

                    </h3>

                    <Select
                        value={cuotaSeleccionada}
                        options={cuotas}
                        onChange={(valor) => setCuotaSeleccionada(Number(valor))}
                        placeholder={null}
                    />

                    <div className="texto-cuotas">

                        Podrás seleccionar entre <strong>3</strong> y <strong>24 cuotas.</strong>

                    </div>

                </div>

                <div className="financiar-footer">

                    <BackButton
                        onClick={volver}
                        texto="Volver"
                    />

                    <PrimaryButton
                        onClick={continuarPaso}
                        className="btn-continuar"
                    >

                        Continuar

                    </PrimaryButton>

                </div>

            </div>

        </div>

    );

}

export default Paso2;