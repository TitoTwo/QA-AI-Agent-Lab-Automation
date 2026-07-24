import { useEffect, useState } from "react";
import bancoApi from "../../api/bancoApi";

import "./Movimientos.css";

import Header from "../../components/Header/Header";
import BackButton from "../../components/common/BackButton";
import { useScrollToTop } from "../../hooks/useScrollToTop";

import TablaCuenta from "./TablaCuenta";
import TablaCredito from "./TablaCredito";
import TablaDebito from "./TablaDebito";
import TabsMovimientos from "./TabsMovimientos";
import OpcionesProducto from "./OpcionesProducto";
import TablaCuotas from "./TablaCuotas";

function Movimientos({

    producto,

    volver,

    onAbrirFlujo

}) {

    useScrollToTop();

    const [datos, setDatos] = useState(null);

    const [resumenTarjeta, setResumenTarjeta] = useState(null);

    const [tabActiva, setTabActiva] = useState("movimientos");

    useEffect(() => {

        const cargarMovimientos = async () => {

            try {

                let response;

                if (producto.tipo === "CUENTA") {

                    response = await bancoApi.get(

                        `/movimientos/cuenta/${producto.id}`

                    );

                    setDatos(response.data);

                }

                if (

                    producto.tipo === "CREDITO" ||

                    producto.tipo === "DEBITO"

                ) {

                    response = await bancoApi.get(

                        `/tarjetas/${producto.id}/movimientos`

                    );

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


    if (!datos) {

        return <h2>Cargando movimientos...</h2>;

    }

    console.log("Producto:", producto);

    console.log("Resumen:", resumenTarjeta);

    return (

        <div className="home-container">

            <Header />

            <div className="movimientos-top">

                <BackButton

                    onClick={volver}

                    texto="Volver"

                />

                <h2 className="section-title">

                    Movimientos

                </h2>

                <div className="producto-nombre">

                    {producto.nombre}

                </div>

            </div>

            <TabsMovimientos

                tabActiva={tabActiva}

                cambiarTab={setTabActiva}

                mostrarCuotas={producto.tipo === "CREDITO"}

            />

            {tabActiva === "movimientos" && (

                <>

                    {producto.tipo === "CUENTA" && (

                        <TablaCuenta

                            datos={datos}

                        />

                    )}

                    {producto.tipo === "DEBITO" && (

                        <TablaDebito

                            datos={datos}

                        />

                    )}

                    {producto.tipo === "CREDITO" && (

                        <TablaCredito

                            datos={datos}

                            resumenTarjeta={resumenTarjeta}

                        />

                    )}

                </>

            )}

            {tabActiva === "cuotas" &&
                producto.tipo === "CREDITO" && (

                <TablaCuotas

                    tarjeta={producto}

                />

            )}

            {tabActiva === "opciones" && (

                <OpcionesProducto

                    producto={producto}

                    onFinanciarSaldo={() => {

                        console.log("Producto:", producto);

                        console.log("Resumen:", resumenTarjeta);

                        const tarjetaCompleta = {

                            ...producto,

                            ...resumenTarjeta

                        };

                        console.log("Tarjeta completa:", tarjetaCompleta);

                        onAbrirFlujo(

                            "FINANCIAR",

                            tarjetaCompleta

                        );

                    }}

                />

            )}

        </div>

    );

}

export default Movimientos;