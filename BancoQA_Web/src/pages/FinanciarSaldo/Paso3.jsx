import { useScrollToTop } from "../../hooks/useScrollToTop";

import Header from "../../components/Header/Header";
import BackButton from "../../components/common/BackButton";
import PrimaryButton from "../../components/common/PrimaryButton";
import StepIndicator from "../../components/common/StepIndicator";
import Card from "../../components/common/Card";

import { formatoMoneda } from "../../utils/formatoMoneda";

import "./FinanciarSaldo.css";
import "./Paso3.css";

function Paso3({

    tarjeta,

    simulacion,

    volver,

    confirmar,

    cerrar

}) {

    useScrollToTop();

    if (!simulacion) {

        return null;

    }

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

                    paso={3}

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

                        Confirmá tu financiación

                    </h3>

                    <Card className="tarjeta-box">

                        <div className="resumen-row">

                            <span className="resumen-label">

                                Monto a financiar

                            </span>

                            <span className="resumen-value">

                                {formatoMoneda(simulacion.monto, "ARS")}

                            </span>

                        </div>

                        <div className="resumen-row">

                            <span className="resumen-label">

                                Cantidad de cuotas

                            </span>

                            <span className="resumen-value">

                                {simulacion.cuotas} cuotas

                            </span>

                        </div>

                        <div className="resumen-row">

                            <span className="resumen-label">

                                Valor estimado por cuota

                            </span>

                            <span className="resumen-value">

                                {formatoMoneda(simulacion.valor_cuota, "ARS")}

                            </span>

                        </div>

                        <div className="resumen-row">

                            <span className="resumen-label">

                                Tasa Nominal Anual (TNA)

                            </span>

                            <span className="resumen-value">

                                {simulacion.tna} %

                            </span>

                        </div>

                        <div className="resumen-row">

                            <span className="resumen-label">

                                Costo Financiero Total (CFT)

                            </span>

                            <span className="resumen-value">

                                {simulacion.cft} %

                            </span>

                        </div>

                        <div className="resumen-row resumen-total">

                            <span className="resumen-label">

                                Total estimado a pagar

                            </span>

                            <span className="resumen-value">

                                {formatoMoneda(simulacion.total, "ARS")}

                            </span>

                        </div>

                    </Card>

                    <div className="texto-confirmacion">

                        Al confirmar, el monto será financiado en la tarjeta seleccionada y las cuotas se incorporarán automáticamente al resumen mensual.

                    </div>

                    <div className="texto-confirmacion">

                        Los importes son estimativos y pueden variar según las condiciones vigentes al momento de la liquidación.

                    </div>

                </div>

                <div className="financiar-footer">

                    <BackButton

                        onClick={volver}

                    />

                    <PrimaryButton

                        onClick={confirmar}

                    >

                        Confirmar

                    </PrimaryButton>

                </div>

            </div>

        </div>

    );

}

export default Paso3;