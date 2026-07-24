import Card from "../../components/common/Card";

import "./OpcionesProducto.css";

function OpcionesProducto({

    producto,

    onFinanciarSaldo

}) {

    const esCredito = producto.tipo === "CREDITO";

    const opciones = [];

    if (esCredito) {

        opciones.push({

            id: "financiar",

            titulo: "Financiar saldo",

            descripcion: "Convertí el saldo de tu tarjeta en cuotas.",

            accion: onFinanciarSaldo

        });

    }

    opciones.push({

        id: "limites",

        titulo: "Consultar límites",

        descripcion: "Visualizá los límites disponibles.",

        accion: () => {}

    });

    opciones.push({

        id: "bloquear",

        titulo: "Bloquear producto",

        descripcion: "Bloqueá temporalmente tu producto.",

        accion: () => {}

    });

    opciones.push({

        id: "resumen",

        titulo: "Descargar resumen",

        descripcion: "Obtené el último resumen disponible.",

        accion: () => {}

    });

    return (

        <div className="opciones-grid">

            {opciones.map((opcion) => (

                <Card

                    key={opcion.id}

                    className="opcion-card"

                    onClick={opcion.accion}

                >

                    <div className="opcion-titulo">

                        {opcion.titulo}

                    </div>

                    <div className="opcion-descripcion">

                        {opcion.descripcion}

                    </div>

                </Card>

            ))}

        </div>

    );

}

export default OpcionesProducto;