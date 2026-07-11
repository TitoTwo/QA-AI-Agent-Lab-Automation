import "./ProductoMenu.css";

function ProductoMenu({
    acciones,
    onSeleccionar
}) {

    const textos = {
        VER_MOVIMIENTOS: "Ver movimientos",
        FINANCIAR_SALDO: "Financiar saldo"
    };

    return (

        <div className="producto-menu-popup">

            {acciones.map((accion) => (

                <button
                    key={accion}
                    className="producto-menu-item"
                    onClick={() => onSeleccionar(accion)}
                >
                    {textos[accion]}
                </button>

            ))}

        </div>

    );

}

export default ProductoMenu;