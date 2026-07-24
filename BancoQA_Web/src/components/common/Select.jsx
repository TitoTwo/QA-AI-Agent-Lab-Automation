import "./common.css";

function Select({
    value,
    options,
    onChange,
    placeholder = "Seleccioná una opción"
}) {

    return (

        <div className="select-common-container">

            <select
                className="select-common"
                value={value}
                onChange={(e) => onChange(e.target.value)}
            >

                {placeholder && (
                    <option value="" disabled>
                        {placeholder}
                    </option>
                )}

                {options.map((option) => (

                    <option
                        key={option.value}
                        value={option.value}
                    >
                        {option.label}
                    </option>

                ))}

            </select>

            <span className="select-common-arrow">
                ▼
            </span>

        </div>

    );

}

export default Select;