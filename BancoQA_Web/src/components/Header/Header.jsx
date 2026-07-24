import "./Header.css";

function Header({
    mostrarBanner = true,
    mostrarSalir = false,
    salir,
    titulo,
    mostrarCerrar = false,
    cerrar
}) {

    return (

        <>

            <div className="header-app">

                <div className="header-logo">

                    Banco QA

                </div>

                <div className="header-right">

                    {titulo && (

                        <span className="header-title">

                            {titulo}

                        </span>

                    )}

                    {mostrarSalir && (

                        <button
                            className="header-salir"
                            onClick={salir}
                        >

                            Salir

                        </button>

                    )}

                    {mostrarCerrar && (

                        <button
                            className="btn-cerrar-header"
                            onClick={cerrar}
                        >

                            ✕

                        </button>

                    )}

                </div>

            </div>

        </>

    );

}

export default Header;