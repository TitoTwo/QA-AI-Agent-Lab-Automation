movimientos = [

    # Movimiento generado con tarjeta débito 102
    {
        "id": 90001,
        "fecha": "2026-06-20",
        "hora": "10:30",
        "cuenta_id": 5001,
        "tarjeta_id": 102,
        "tipo": "COMPRA",
        "categoria": "COMERCIO",
        "descripcion": "Supermercado",
        "importe": -25000,
        "moneda": "ARS",
        "estado": "CONFIRMADO"
    },


    {
        "id": 90002,
        "fecha": "2026-06-21",
        "hora": "15:20",
        "cuenta_id": 5001,
        "tarjeta_id": 102,
        "tipo": "EXTRACCION",
        "categoria": "CAJERO",
        "descripcion": "Extracción cajero automático",
        "importe": -50000,
        "moneda": "ARS",
        "estado": "CONFIRMADO"
    },


    # Movimiento propio de cuenta
    {
        "id": 90003,
        "fecha": "2026-06-01",
        "hora": "08:00",
        "cuenta_id": 5001,
        "tarjeta_id": None,
        "tipo": "DEPOSITO",
        "categoria": "INGRESO",
        "descripcion": "Acreditación sueldo",
        "importe": 500000,
        "moneda": "ARS",
        "estado": "CONFIRMADO"
    },


    {
        "id": 90004,
        "fecha": "2026-06-15",
        "hora": "12:40",
        "cuenta_id": 5001,
        "tarjeta_id": None,
        "tipo": "TRANSFERENCIA",
        "categoria": "TRANSFERENCIA",
        "descripcion": "Transferencia enviada",
        "importe": -30000,
        "moneda": "ARS",
        "estado": "CONFIRMADO"
    },


    # Tarjeta crédito VISA 101
    {
        "id": 90005,
        "fecha": "2026-06-18",
        "hora": "20:10",
        "cuenta_id": None,
        "tarjeta_id": 101,
        "tipo": "COMPRA",
        "categoria": "COMERCIO",
        "descripcion": "Restaurante",
        "importe": -35000,
        "moneda": "ARS",
        "estado": "CONFIRMADO"
    },


    {
        "id": 90006,
        "fecha": "2026-06-19",
        "hora": "17:30",
        "cuenta_id": None,
        "tarjeta_id": 101,
        "tipo": "COMPRA",
        "categoria": "ONLINE",
        "descripcion": "Compra online",
        "importe": -15000,
        "moneda": "ARS",
        "estado": "CONFIRMADO"
    }

]