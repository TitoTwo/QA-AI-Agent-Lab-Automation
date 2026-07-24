import "./common.css";

function DownloadReceiptButton({

    onClick

}) {

    return (

        <button

            type="button"

            className="btn-download-common"

            onClick={onClick}

        >

            📄 Descargar comprobante

        </button>

    );

}

export default DownloadReceiptButton;