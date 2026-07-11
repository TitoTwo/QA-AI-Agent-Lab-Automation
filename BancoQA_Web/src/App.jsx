import { useState } from "react";

import Login from "./components/Login";
import Home from "./components/Home";

function App() {

    const [cliente, setCliente] = useState(null);

    const cerrarSesion = () => {

        setCliente(null);

    };

    return (

        <div>

            {

                cliente ?

                    <Home
                        cliente={cliente}
                        salir={cerrarSesion}
                    />

                :

                    <Login
                        setCliente={setCliente}
                    />

            }

        </div>

    );

}

export default App;