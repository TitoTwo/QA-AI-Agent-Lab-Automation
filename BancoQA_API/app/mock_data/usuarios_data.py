usuarios = [

    # Perfil premium con caja de ahorro en pesos, dólares y euros, cuenta corriente, tarjetas Visa y Mastercard, movimientos frecuentes y compras en cuotas.
    {
        "id": 1,
        "cliente_id": 1,
        "usuario": "alan.lopez",
        "password": "123456",
        "estado": "ACTIVO"
    },

    # Perfil gold con caja de ahorro y cuenta corriente, movimientos regulares y una tarjeta Visa activa.
    {
        "id": 2,
        "cliente_id": 2,
        "usuario": "maria.gomez",
        "password": "abcdef",
        "estado": "ACTIVO"
    },

    # Perfil básico con una caja de ahorro en pesos y una tarjeta Visa de uso simple.
    {
        "id": 3,
        "cliente_id": 3,
        "usuario": "rocio.iturre",
        "password": "111111",
        "estado": "ACTIVO"
    },

    # Usuario bloqueado para pruebas de acceso con estado inactivo en el sistema.
    {
        "id": 4,
        "cliente_id": 4,
        "usuario": "usuario.bloqueado",
        "password": "999999",
        "estado": "BLOQUEADO"
    }
]

# Usuarios adicionales para pruebas QA con descripción del perfil
usuarios.extend([

    # Usuario básico con caja de ahorro en pesos, tarjeta débito y pocos movimientos.
    {
        "id": 5,
        "cliente_id": 5,
        "usuario": "cliente.basico",
        "password": "basico123",
        "estado": "ACTIVO"
    },

    # Usuario intermedio con caja de ahorro y cuenta corriente, débito y crédito básico, y movimientos regulares.
    {
        "id": 6,
        "cliente_id": 6,
        "usuario": "cliente.medio",
        "password": "medio123",
        "estado": "ACTIVO"
    },

    # Usuario gold con caja de ahorro, cuenta corriente, Visa Gold y compras en cuotas.
    {
        "id": 7,
        "cliente_id": 7,
        "usuario": "cliente.gold",
        "password": "gold123",
        "estado": "ACTIVO"
    },

    # Usuario platinum con cuentas multimoneda, tarjetas premium y operaciones internacionales.
    {
        "id": 8,
        "cliente_id": 8,
        "usuario": "cliente.platinum",
        "password": "platinum123",
        "estado": "ACTIVO"
    },

    # Usuario signature con múltiples cuentas y tarjetas, consumos elevados y compras internacionales.
    {
        "id": 9,
        "cliente_id": 9,
        "usuario": "cliente.signature",
        "password": "signature123",
        "estado": "ACTIVO"
    },

    # Usuario empresarial con cuenta corriente, múltiples transferencias y pagos a proveedores.
    {
        "id": 10,
        "cliente_id": 10,
        "usuario": "cliente.empresa",
        "password": "empresa123",
        "estado": "ACTIVO"
    },

    # Usuario sin movimientos, útil para validar pantallas vacías y estados iniciales.
    {
        "id": 11,
        "cliente_id": 11,
        "usuario": "cliente.sinmov",
        "password": "sinmov123",
        "estado": "ACTIVO"
    },

    # Usuario con muchos movimientos, pensado para pruebas de paginación y rendimiento.
    {
        "id": 12,
        "cliente_id": 12,
        "usuario": "cliente.muchosmov",
        "password": "muchos123",
        "estado": "ACTIVO"
    },

    # Usuario con cuentas en pesos únicamente y un perfil de consumo simple.
    {
        "id": 13,
        "cliente_id": 13,
        "usuario": "cliente.pesos",
        "password": "pesos123",
        "estado": "ACTIVO"
    },

    # Usuario multimoneda con cajas de ahorro en pesos, dólares y euros.
    {
        "id": 14,
        "cliente_id": 14,
        "usuario": "cliente.multimoneda",
        "password": "multi123",
        "estado": "ACTIVO"
    }

])

usuarios.extend([
    # Usuario con tarjeta bloqueada para validar flujos de estado y bloqueo.
    {
        "id": 15,
        "cliente_id": 15,
        "usuario": "cliente.tarjeta.bloqueada",
        "password": "bloq123",
        "estado": "ACTIVO"
    },
    # Usuario con tarjeta vencida para validar renovaciones y errores de vencimiento.
    {
        "id": 16,
        "cliente_id": 16,
        "usuario": "cliente.tarjeta.vencida",
        "password": "venc123",
        "estado": "ACTIVO"
    }
])