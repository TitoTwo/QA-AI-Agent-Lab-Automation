import { formatoMoneda } from "../../utils/formatoMoneda";

function TablaDebito({ datos }) {

    return (

        <table className="movimientos-table">

            <thead>

                <tr>

                    <th>Fecha</th>
                    <th>Detalle</th>
                    <th>Importe</th>

                </tr>

            </thead>

            <tbody>

                {datos.map((movimiento) => (

                    <tr key={movimiento.id}>

                        <td>

                            {movimiento.fecha}

                        </td>

                        <td>

                            {movimiento.descripcion}

                            {movimiento.comercio && (

                                <div className="movimiento-comercio">

                                    {movimiento.comercio}

                                </div>

                            )}

                        </td>

                        <td className="importe-negativo">

                            {formatoMoneda(
                                movimiento.monto,
                                movimiento.moneda
                            )}

                        </td>

                    </tr>

                ))}

            </tbody>

        </table>

    );

}

export default TablaDebito;