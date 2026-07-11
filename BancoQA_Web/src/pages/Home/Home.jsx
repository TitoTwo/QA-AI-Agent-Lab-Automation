import { useEffect, useState } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import bancoApi from "../../api/bancoApi";
import Movimientos from "../Movimientos/Movimientos";
import "./Home.css";
import { formatoMoneda } from "../../utils/formatoMoneda";
import Header from "../../components/Header/Header";
import ProductoMenu from "../../components/ProductoMenu/ProductoMenu";

function Home({ cliente, salir }) {

    const [datosHome, setDatosHome] = useState(null);
    const [productoSeleccionado, setProductoSeleccionado] = useState(null);
    const [mostrarSaldos, setMostrarSaldos] = useState(true);

    const [menuAbierto, setMenuAbierto] = useState(null);

    useEffect(() => {

        const cargarHome = async () => {

            try {

                const response = await bancoApi.get(`/clientes/${cliente.id}/home`);
                setDatosHome(response.data);

            } catch (error) {

                console.log(error);
                alert("Error cargando información del cliente");

            }

        };

        cargarHome();

    }, [cliente]);

    if (!datosHome) {

        return <h2>Cargando información...</h2>;

    }

    if (productoSeleccionado) {

        return (
            <Movimientos
                producto={productoSeleccionado}
                volver={() => setProductoSeleccionado(null)}
            />
        );

    }

    return (

        <div className="home-container">

            <Header
                mostrarSalir={true}
                salir={salir}
            />

            <div className="productos-header">

                <h2>Mis productos</h2>

                <button
                    className="ocultar-saldos"
                    onClick={() => setMostrarSaldos(!mostrarSaldos)}
                >

                    {mostrarSaldos ? (
                        <>
                            Ocultar saldos&nbsp;
                            <FaEye />
                        </>
                    ) : (
                        <>
                            Mostrar saldos&nbsp;
                            <FaEyeSlash />
                        </>
                    )}

                </button>

            </div>

            <h2 className="section-title">
                Cuentas
            </h2>

            <div className="productos-lista">

                {datosHome.cuentas.map((cuenta) => (

                    <div
                        key={cuenta.id}
                        className="producto-row"
                        onClick={() =>
                            setProductoSeleccionado({
                                tipo: "CUENTA",
                                id: cuenta.id,
                                nombre: cuenta.nombre,
                                moneda: cuenta.moneda
                            })
                        }
                    >

                        <div className="producto-info">

                            <div className="producto-title">
                                {cuenta.nombre}
                            </div>

                            <div className="producto-numero">
                                {cuenta.id}
                            </div>

                        </div>

                        <div className="producto-saldos">

                            <div className="producto-saldo">

                                {mostrarSaldos
                                    ? formatoMoneda(cuenta.saldo, cuenta.moneda)
                                    : "$ ******"}

                                <span>Saldo</span>

                            </div>

                            {cuenta.acuerdo && (

                                <div className="producto-saldo">

                                    {mostrarSaldos
                                        ? formatoMoneda(cuenta.acuerdo, cuenta.moneda)
                                        : "$ ******"}

                                    <span>Acuerdo</span>

                                </div>

                            )}

                        </div>

                        <div
                            className="producto-menu"
                            onClick={(e) => {

                                e.stopPropagation();

                                setMenuAbierto(
                                    menuAbierto === `cuenta-${cuenta.id}`
                                        ? null
                                        : `cuenta-${cuenta.id}`
                                );

                            }}
                        >

                            ⋮

                            {menuAbierto === `cuenta-${cuenta.id}` && (

                                <ProductoMenu

                                    acciones={[
                                        "VER_MOVIMIENTOS"
                                    ]}

                                    onSeleccionar={(accion) => {

                                        switch (accion) {

                                            case "VER_MOVIMIENTOS":

                                                setProductoSeleccionado({
                                                    tipo: "CUENTA",
                                                    id: cuenta.id,
                                                    nombre: cuenta.nombre,
                                                    moneda: cuenta.moneda
                                                });

                                                break;

                                            default:
                                                break;

                                        }

                                        setMenuAbierto(null);

                                    }}

                                />

                            )}

                        </div>

                    </div>

                ))}

            </div>

            <h2 className="section-title">
                Tarjetas
            </h2>

            <div className="productos-lista">

                {datosHome.tarjetas.map((tarjeta) => (

                    <div
                        key={tarjeta.id}
                        className="producto-row tarjeta-row"
                        onClick={() =>
                            setProductoSeleccionado({
                                tipo: tarjeta.tipo,
                                id: tarjeta.id,
                                nombre: tarjeta.nombre,
                                saldo_pesos: tarjeta.saldo_pesos,
                                saldo_dolares: tarjeta.saldo_dolares
                            })
                        }
                    >

                        <div className="producto-info">

                            <div className="producto-title">
                                {tarjeta.nombre}
                            </div>

                            <div className="producto-numero">
                                {tarjeta.numero}
                            </div>

                        </div>
                                                {tarjeta.tipo === "CREDITO" ? (

                            <div className="tarjeta-saldos">

                                <div className="tarjeta-saldo">

                                    <div className="tarjeta-monto">

                                        {mostrarSaldos
                                            ? formatoMoneda(tarjeta.saldo_pesos, "ARS")
                                            : "$ ******"}

                                    </div>

                                    <div className="tarjeta-texto">
                                        Saldo en pesos
                                    </div>

                                </div>

                                <div className="tarjeta-saldo">

                                    <div className="tarjeta-monto">

                                        {mostrarSaldos
                                            ? formatoMoneda(tarjeta.saldo_dolares, "USD")
                                            : "U$S ******"}

                                    </div>

                                    <div className="tarjeta-texto">
                                        Saldo en dólares
                                    </div>

                                </div>

                            </div>

                        ) : (

                            <div className="tarjeta-saldos">

                                <div className="tarjeta-saldo">

                                    <div className="tarjeta-texto">
                                        Tarjeta de débito
                                    </div>

                                </div>

                            </div>

                        )}

                        <div
                            className="producto-menu"
                            onClick={(e) => {

                                e.stopPropagation();

                                setMenuAbierto(
                                    menuAbierto === `tarjeta-${tarjeta.id}`
                                        ? null
                                        : `tarjeta-${tarjeta.id}`
                                );

                            }}
                        >

                            ⋮

                            {menuAbierto === `tarjeta-${tarjeta.id}` && (

                                <ProductoMenu

                                    acciones={
                                        tarjeta.tipo === "CREDITO"
                                            ? [
                                                "VER_MOVIMIENTOS",
                                                "FINANCIAR_SALDO"
                                            ]
                                            : [
                                                "VER_MOVIMIENTOS"
                                            ]
                                    }

                                    onSeleccionar={(accion) => {

                                        switch (accion) {

                                            case "VER_MOVIMIENTOS":

                                                setProductoSeleccionado({
                                                    tipo: tarjeta.tipo,
                                                    id: tarjeta.id,
                                                    nombre: tarjeta.nombre,
                                                    saldo_pesos: tarjeta.saldo_pesos,
                                                    saldo_dolares: tarjeta.saldo_dolares
                                                });

                                                break;

                                            case "FINANCIAR_SALDO":

                                                console.log(
                                                    "Ir a financiar saldo",
                                                    tarjeta.id
                                                );

                                                // Próximo paso:
                                                // setPantalla("FINANCIAR_SALDO")

                                                break;

                                            default:
                                                break;

                                        }

                                        setMenuAbierto(null);

                                    }}

                                />

                            )}

                        </div>

                    </div>

                ))}

            </div>

        </div>

    );

}

export default Home;