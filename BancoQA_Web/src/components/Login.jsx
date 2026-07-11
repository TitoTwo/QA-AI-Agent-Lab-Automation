import { useState } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import bancoApi from "../Api/bancoApi";
import "../styles/Login.css";
import Header from "../components/Header";

function Login({ setCliente }) {

    const [tipoDocumento, setTipoDocumento] = useState("DNI");
    const [documento, setDocumento] = useState("");
    const [usuario, setUsuario] = useState("");
    const [clave, setClave] = useState("");

    const [mostrarUsuario, setMostrarUsuario] = useState(false);
    const [mostrarClave, setMostrarClave] = useState(false);

    const [mensajeError, setMensajeError] = useState("");

    const loginHabilitado =
        documento.trim() !== "" &&
        usuario.trim() !== "" &&
        clave.trim() !== "";

    const iniciarSesion = async () => {

        if (!loginHabilitado) return;

        setMensajeError("");

        try {

            const response = await bancoApi.post("/auth/login", {
                tipo_documento: tipoDocumento,
                documento,
                usuario,
                password: clave
            });

            setCliente(response.data.cliente);

        } catch (error) {

            if (error.response?.data?.detail) {

                setMensajeError(error.response.data.detail);

            } else {

                setMensajeError(
                    "No fue posible conectarse con el servidor. Intentá nuevamente."
                );

            }

        }

    };

    return (

        <div className="login-page">

            <Header
            />

            <div className="login-card">

                <h1>

                    ¡Hola!
                    <br />
                    Te damos la bienvenida a Banca Online

                </h1>

                <div className="campo">

                    <label>

                        Tipo de documento

                    </label>

                    <select
                        value={tipoDocumento}
                        onChange={(e) => setTipoDocumento(e.target.value)}
                    >

                        <option>DNI</option>

                        <option>PASAPORTE</option>

                    </select>

                </div>

                <div className="campo">

                    <label>

                        Número de documento

                    </label>

                    <input
                        type="text"
                        value={documento}
                        onChange={(e) => setDocumento(e.target.value)}
                    />

                </div>

                <div className="campo">

                    <label>

                        Usuario

                    </label>

                    <div className="input-icono">

                        <input
                            type={mostrarUsuario ? "text" : "password"}
                            value={usuario}
                            onChange={(e) => setUsuario(e.target.value)}
                        />

                        <button
                            type="button"
                            className="icono-ojo"
                            onClick={() => setMostrarUsuario(!mostrarUsuario)}
                        >

                            {mostrarUsuario
                                ? <FaEye />
                                : <FaEyeSlash />
                            }

                        </button>

                    </div>

                </div>

                <div className="campo">

                    <label>

                        Clave

                    </label>

                    <div className="input-icono">

                        <input
                            type={mostrarClave ? "text" : "password"}
                            value={clave}
                            onChange={(e) => setClave(e.target.value)}
                        />

                        <button
                            type="button"
                            className="icono-ojo"
                            onClick={() => setMostrarClave(!mostrarClave)}
                        >

                            {mostrarClave
                                ? <FaEye />
                                : <FaEyeSlash />
                            }

                        </button>

                    </div>

                </div>

                {mensajeError && (

                    <div className="login-error">

                        {mensajeError}

                    </div>

                )}

                <div className="recordar">

                    <input
                        type="checkbox"
                        id="recordar"
                    />

                    <label htmlFor="recordar">

                        Recordar mi documento y usuario

                    </label>

                </div>

                <button
                    className="btn-login"
                    disabled={!loginHabilitado}
                    onClick={iniciarSesion}
                >

                    Ingresar

                </button>

            </div>

        </div>

    );

}

export default Login;