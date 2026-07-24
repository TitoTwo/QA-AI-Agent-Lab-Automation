clientes = [

    {
        "id": 1,
        "nombre": "Alan López",
        "tipo_documento":"DNI",
        "documento": "30111222",
        "categoria": 4
    },


    {
        "id": 2,
        "nombre": "Maria Gomez",
        "tipo_documento":"DNI",
        "documento": "30222333",
        "categoria": 2
    },


    {
        "id": 3,
        "nombre": "Rocio Iturre",
        "tipo_documento":"DNI",
        "documento": "30444555",
        "categoria": 1
    },


    {
        "id": 4,
        "nombre": "Usuario Bloqueado",
        "tipo_documento":"DNI",
        "documento": "30424545",
        "categoria": 1
    }
]

# ==========================
# CLIENTES ADICIONALES PARA PRUEBAS QA
# ==========================

clientes.extend([

    {
        "id": 5,
        "nombre": "Cliente Básico",
        "tipo_documento":"DNI",
        "documento": "30500101",
        "categoria": 1
    },

    {
        "id": 6,
        "nombre": "Cliente Medio",
        "tipo_documento":"DNI",
        "documento": "30500202",
        "categoria": 2
    },

    {
        "id": 7,
        "nombre": "Cliente Gold",
        "tipo_documento":"DNI",
        "documento": "30500303",
        "categoria": 3
    },

    {
        "id": 8,
        "nombre": "Cliente Platinum",
        "tipo_documento":"DNI",
        "documento": "30500404",
        "categoria": 4
    },

    {
        "id": 9,
        "nombre": "Cliente Signature",
        "tipo_documento":"DNI",
        "documento": "30500505",
        "categoria": 4
    },

    {
        "id": 10,
        "nombre": "Cliente Empresa SA",
        "tipo_documento":"CUIT",
        "documento": "30500606",
        "categoria": 4
    },

    {
        "id": 11,
        "nombre": "Cliente Sin Movimientos",
        "tipo_documento":"DNI",
        "documento": "30500707",
        "categoria": 1
    },

    {
        "id": 12,
        "nombre": "Cliente Muchos Movimientos",
        "tipo_documento":"DNI",
        "documento": "30500808",
        "categoria": 2
    },

    {
        "id": 13,
        "nombre": "Cliente Pesos Unicamente",
        "tipo_documento":"DNI",
        "documento": "30500909",
        "categoria": 1
    },

    {
        "id": 14,
        "nombre": "Cliente Multimoneda",
        "tipo_documento":"DNI",
        "documento": "30501010",
        "categoria": 4
    }

])

# Clientes para tarjetas con estado especial
clientes.extend([
    {
        "id": 15,
        "nombre": "Cliente Tarjeta Bloqueada",
        "tipo_documento":"DNI",
        "documento": "30501111",
        "categoria": 2
    },
    {
        "id": 16,
        "nombre": "Cliente Tarjeta Vencida",
        "tipo_documento":"DNI",
        "documento": "30501212",
        "categoria": 2
    }
])