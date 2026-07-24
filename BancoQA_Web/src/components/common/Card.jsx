import "./common.css";

function Card({ children, className = "", onClick }) {
    return (
        <div
            className={`card-common tarjeta-box ${className}`}
            onClick={onClick}
        >
            {children}
        </div>
    );
}

export default Card;
