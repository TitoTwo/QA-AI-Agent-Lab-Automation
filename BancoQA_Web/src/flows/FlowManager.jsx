import FinanciarSaldo from "../pages/FinanciarSaldo/FinanciarSaldo";

function FlowManager({

    flujo,

    producto,

    volver

}) {

    switch (flujo) {

        case "FINANCIAR":

            return (

                <FinanciarSaldo

                    tarjeta={producto}

                    volver={volver}

                />

            );

        default:

            return null;

    }

}

export default FlowManager;