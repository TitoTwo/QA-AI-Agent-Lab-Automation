import { formatoMoneda } from "../../utils/formatoMoneda";

function TablaCredito({

    datos,

    resumenTarjeta

}) {

    return (

        <>

            <div className="tarjeta-resumen">

                <div className="tarjeta-resumen-item">

                    <div className="tarjeta-resumen-texto">

                        Saldo en pesos

                    </div>

                    <div className="tarjeta-resumen-monto">

                        {formatoMoneda(
                            resumenTarjeta.saldo_pesos,
                            "ARS"
                        )}

                    </div>

                </div>

                <div className="tarjeta-resumen-item">

                    <div className="tarjeta-resumen-texto">

                        Saldo en dólares

                    </div>

                    <div className="tarjeta-resumen-monto">

                        {formatoMoneda(
                            resumenTarjeta.saldo_dolares,
                            "USD"
                        )}

                    </div>

                </div>

            </div>

            <table className="movimientos-table">

                <thead>

                    <tr>

                        <th>Fecha</th>
                        <th>Detalle</th>
                        <th>Cuota</th>
                        <th>Monto</th>

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

                            <td>

                                {movimiento.cuotas

                                    ? `${movimiento.cuotas.actual}/${movimiento.cuotas.total}`

                                    : "-"}

                            </td>

                            <td>
                                {formatoMoneda(
                                    movimiento.monto_visible ?? Math.abs(movimiento.monto),
                                    movimiento.moneda
                                )}
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </>

    );

}

export default TablaCredito;