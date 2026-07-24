import "./common.css";

function PrimaryButton({

    children,

    onClick,

    disabled = false,

    className = ""

}) {

    return (

        <button
            type="button"
            onClick={onClick}
            disabled={disabled}
            className={`btn-continuar-common ${className}`}
        >

            {children}

        </button>

    );

}

export default PrimaryButton;

