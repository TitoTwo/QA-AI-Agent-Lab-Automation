import { ArrowLeft } from "lucide-react";
import "./common.css";

function BackButton({

    onClick,

    texto = "Volver",

    className = ""

}) {

    return (

        <button
            type="button"
            onClick={onClick}
            className={`btn-volver-common ${className}`}
        >

            <ArrowLeft
                className="flecha-volver-common"
                aria-hidden="true"
            />

            <span>

                {texto}

            </span>

        </button>

    );

}

export default BackButton;


