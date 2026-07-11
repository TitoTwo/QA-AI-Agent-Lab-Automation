import "../styles/Header.css";

function Header({
    mostrarBanner = false,
    mostrarSalir = false,
    salir
}) {

    return (

        <>

            {mostrarBanner && (

                <div className="header-banner">

                    {/* Aquí luego irá la imagen/banner */}

                </div>

            )}

            <div className="header-app">

                <div className="header-logo">

                    Banco QA

                </div>

                {mostrarSalir && (

                    <button
                        className="header-salir"
                        onClick={salir}
                    >

                        Salir

                    </button>

                )}

            </div>

        </>

    );

}

export default Header;