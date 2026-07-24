import { formatoMoneda } from "../../utils/formatoMoneda";

function TablaCuenta({ datos }) {

    return (

        <table className="movimientos-table">

            <thead>

                <tr>

                    <th>Fecha</th>
                    <th>Detalle</th>
                    <th>Importe</th>
                    <th>Saldo total</th>

                </tr>

            </thead>

            <tbody>

                {datos.map((movimiento) => (

                    <tr key={movimiento.id}>

                        <td>{movimiento.fecha}</td>

                        <td>

                            {movimiento.descripcion}

                            {movimiento.comercio && (

                                <div className="movimiento-comercio">

                                    {movimiento.comercio}

                                </div>

                            )}

                        </td>

                        <td
                            className={
                                movimiento.monto >= 0
                                    ? "importe-positivo"
                                    : "importe-negativo"
                            }
                        >

                            {formatoMoneda(
                                movimiento.monto,
                                movimiento.moneda
                            )}

                        </td>

                        <td>

                            {formatoMoneda(
                                movimiento.saldo_resultante,
                                movimiento.moneda
                            )}

                        </td>

                    </tr>

                ))}

            </tbody>

        </table>

    );

}

export default TablaCuenta;