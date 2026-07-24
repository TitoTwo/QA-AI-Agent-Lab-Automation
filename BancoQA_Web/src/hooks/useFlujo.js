import { useState } from "react";

function useFlujo() {

    const [flujoActivo, setFlujoActivo] = useState(null);

    const abrirFlujo = (nombreFlujo) => {

        setFlujoActivo(nombreFlujo);

    };

    const cerrarFlujo = () => {

        setFlujoActivo(null);

    };

    return {

        flujoActivo,

        abrirFlujo,

        cerrarFlujo

    };

}

export default useFlujo;