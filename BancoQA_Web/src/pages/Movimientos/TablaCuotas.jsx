import { useEffect, useState } from "react";
import bancoApi from "../../api/bancoApi";

import "./TablaCuotas.css";

import { formatoMoneda } from "../../utils/formatoMoneda";

function TablaCuotas({

    tarjeta

}) {

    const [datos, setDatos] = useState(null);

    const [cantidadVisible, setCantidadVisible] = useState(20);

    useEffect(() => {

        const cargarCuotas = async () => {

            try {

                const response = await bancoApi.get(

                    `/tarjetas/${tarjeta.id}/cuotas`

                );

                setDatos(response.data);

            }

            catch (error) {

                console.log(error);

                alert("Error obteniendo cuotas");

            }

        };

        cargarCuotas();

    }, [tarjeta]);

    if (!datos) {

        return <h2>Cargando cuotas...</h2>;

    }

    const cuotasMostradas = datos.cuotas.slice(

        0,

        cantidadVisible

    );

    return (

        <div className="tabla-cuotas-container">

            <div className="tabla-cuotas-header">

                <h3>

                    Detalle de cuotas pendientes

                </h3>

            </div>

            <table className="tabla-cuotas">

                <thead>

                    <tr>

                        <th>Fecha</th>

                        <th>Movimiento</th>

                        <th>Cuota</th>

                        <th>Monto</th>

                        <th>Restante</th>

                    </tr>

                </thead>

                <tbody>

                    {cuotasMostradas.map((cuota) => (

                        <tr key={cuota.id}>

                            <td>

                                {cuota.fecha}

                            </td>

                            <td>

                                {cuota.movimiento}

                            </td>

                            <td>

                                {cuota.cuota}

                            </td>

                            <td>

                                {formatoMoneda(

                                    cuota.monto_cuota,

                                    "ARS"

                                )}

                            </td>

                            <td>

                                {formatoMoneda(

                                    cuota.restante,

                                    "ARS"

                                )}

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

            <div className="cuotas-resumen">

                <div className="resumen-card">

                    <div className="titulo">

                        Próximo vencimiento

                    </div>

                    <div className="valor">

                        {formatoMoneda(

                            datos.proximo_vencimiento,

                            "ARS"

                        )}

                    </div>

                </div>

                <div className="resumen-card">

                    <div className="titulo">

                        Restante Total

                    </div>

                    <div className="valor">

                        {formatoMoneda(

                            datos.restante_total,

                            "ARS"

                        )}

                    </div>

                </div>

            </div>

            <div className="acciones-cuotas">

                <button

                    className="btn-descargar"

                >

                    Descargar

                </button>

            </div>

            {

                cantidadVisible < datos.cuotas.length && (

                    <div className="ver-mas-container">

                        <button

                            className="btn-ver-mas"

                            onClick={() =>

                                setCantidadVisible(

                                    cantidadVisible + 10

                                )

                            }

                        >

                            Ver más

                        </button>

                    </div>

                )

            }

        </div>

    );

}

export default TablaCuotas;