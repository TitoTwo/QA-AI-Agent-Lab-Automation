import "./common.css";

function StepIndicator({

    paso,

    total,

    className = ""

}) {

    return (

        <div className={`paso-indicador-common ${className}`}>

            <strong>

                Paso {paso} de {total}

            </strong>

        </div>

    );

}

export default StepIndicator;