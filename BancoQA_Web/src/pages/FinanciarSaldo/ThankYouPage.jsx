import { useScrollToTop } from "../../hooks/useScrollToTop";

import Header from "../../components/Header/Header";
import PrimaryButton from "../../components/common/PrimaryButton";
import DownloadReceiptButton from "../../components/common/DownloadReceiptButton";
import { formatoMoneda } from "../../utils/formatoMoneda";
import { generarComprobantePDF } from "../../utils/generarComprobantePDF";
import "./FinanciarSaldo.css";
import "./ThankYouPage.css";

function ThankYouPage({

    tarjeta,

    operacion,

    volver,

    cerrar

}) {

    useScrollToTop();

    if (!operacion) {

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

            <div className="thankyou-container">

                <div className="thankyou-icon">

                    ✓

                </div>

                <h2 className="thankyou-title">

                    ¡Listo! Tu financiación fue realizada con éxito

                </h2>

                <p className="thankyou-text">

                    Financiaste <strong>

                        {formatoMoneda(operacion.monto, "ARS")}

                    </strong> de tu tarjeta <strong>

                        {tarjeta.nombre}

                    </strong> en <strong>

                        {operacion.cuotas} cuotas

                    </strong>.

                </p>

                <p className="thankyou-text">

                    Pagarás aproximadamente <strong>

                        {operacion.cuotas} cuotas de{" "}

                        {formatoMoneda(operacion.valor_cuota, "ARS")}

                    </strong>, alcanzando un total estimado de <strong>

                        {formatoMoneda(operacion.total, "ARS")}

                    </strong>. La operación quedó registrada con el número <strong>

                        {operacion.numero_operacion}

                    </strong>, el día <strong>

                        {operacion.fecha_operacion}

                    </strong>.

                </p>

                <p className="thankyou-message">

                    En las próximas horas podrás visualizar la financiación reflejada en el resumen de tu tarjeta.

                </p>

                <div className="thankyou-footer">

                    <PrimaryButton

                        onClick={volver}

                    >

                        Finalizar

                    </PrimaryButton>

                </div>

                <DownloadReceiptButton

                    onClick={() =>

                        generarComprobantePDF(

                            tarjeta,

                            operacion

                        )

                    }

                />

            </div>

        </div>

    );

}

export default ThankYouPage;