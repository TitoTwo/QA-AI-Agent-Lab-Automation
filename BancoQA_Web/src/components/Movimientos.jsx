import { useEffect, useState } from "react";
import bancoApi from "../Api/bancoApi";
import { formatoMoneda } from "../Utils/formatoMoneda";
import "../styles/Movimientos.css";
import { ArrowLeft } from "lucide-react";
import Header from "../components/Header";

function Movimientos({ producto, volver }) {

    const [datos, setDatos] = useState(null);
    const [resumenTarjeta, setResumenTarjeta] = useState(null);

    useEffect(() => {

        const cargarMovimientos = async () => {

            try {

                let response;

                if (producto.tipo === "CUENTA") {

                    response = await bancoApi.get(`/movimientos/cuenta/${producto.id}`);
                    setDatos(response.data);

                }

                if (producto.tipo === "CREDITO" || producto.tipo === "DEBITO") {

                    response = await bancoApi.get(`/tarjetas/${producto.id}/movimientos`);

                    setResumenTarjeta(response.data.tarjeta);
                    setDatos(response.data.movimientos);

                }

            } catch (error) {

                console.log(error);
                alert("Error cargando movimientos");

            }

        };

        cargarMovimientos();

    }, [producto]);

    if (!datos) return <h2>Cargando movimientos...</h2>;

    datos.forEach(m => {
    console.log(
        m.descripcion,
        m.monto,
        typeof m.monto
    );
});

    return (

        <div className="home-container">

            <Header />

            <div className="movimientos-top">

                <button
                    className="btn-volver"
                    onClick={volver}
                >
                    <ArrowLeft
                        className="flecha-volver"
                    />

                    Volver
                </button>

                <h2 className="section-title">
                    Movimientos
                </h2>

                <div className="producto-nombre">
                    {producto.nombre}
                </div>

            </div>

            {producto.tipo === "CUENTA" && (

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

            )}

            {producto.tipo === "CREDITO" && resumenTarjeta && (

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
                                            Math.abs(movimiento.monto),
                                            movimiento.moneda
                                        )}

                                    </td>

                                </tr>

                            ))}

                        </tbody>

                    </table>

                </>

            )}
                        {producto.tipo === "DEBITO" && (

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

            )}

        </div>

    );

}

export default Movimientos;