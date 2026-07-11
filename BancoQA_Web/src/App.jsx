import { useState } from "react";

import Login from "./pages/Login/Login";
import Home from "./pages/Home/Home";

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