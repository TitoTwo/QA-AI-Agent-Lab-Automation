import "./common.css";

function CurrencyInput({

    value,

    onChange,

    helper,

    error,

    placeholder = "Ingrese el importe"

}) {

    return (

        <div className="currency-input-container">

            <div className="currency-input-box">

                <span className="currency-symbol">

                    $

                </span>

                <input

                    type="number"

                    value={value}

                    onChange={onChange}

                    placeholder={placeholder}

                    className="currency-input"

                />

            </div>

            <div className="currency-messages">

                {

                    helper && (

                        <div className="currency-helper">

                            {helper}

                        </div>

                    )

                }

                {

                    error && (

                        <div className="currency-error">

                            {error}

                        </div>

                    )

                }

            </div>

        </div>

    );

}

export default CurrencyInput;