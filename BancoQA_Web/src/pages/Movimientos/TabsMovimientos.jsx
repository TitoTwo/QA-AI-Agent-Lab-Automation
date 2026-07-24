import "./TabsMovimientos.css";

function TabsMovimientos({

    tabActiva,

    cambiarTab,

    mostrarCuotas

}) {

    return (

        <div className="tabs-wrapper">

            <div className="tabs-nav">

                <button

                    className={
                        tabActiva === "movimientos"
                            ? "tab-item active"
                            : "tab-item"
                    }

                    onClick={() => cambiarTab("movimientos")}

                >

                    Consumos del mes

                </button>

                {mostrarCuotas && (

                    <button

                        className={
                            tabActiva === "cuotas"
                                ? "tab-item active"
                                : "tab-item"
                        }

                        onClick={() => cambiarTab("cuotas")}

                    >

                        Cuotas pendientes

                    </button>

                )}

                <button

                    className={
                        tabActiva === "opciones"
                            ? "tab-item active"
                            : "tab-item"
                    }

                    onClick={() => cambiarTab("opciones")}

                >

                    Más opciones

                </button>

            </div>

        </div>

    );

}

export default TabsMovimientos;