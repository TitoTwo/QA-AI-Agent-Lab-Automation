movimientos = [

# =====================================================
# CLIENTE 1 - ALAN LOPEZ - CATEGORIA 4
# =====================================================


# ==========================
# CUENTA 5001 PESOS
# ==========================

{
"id":1,
"cliente_id":1,
"cuenta_id":5001,
"tipo":"CUENTA",
"categoria":"TRANSFERENCIA",
"fecha":"2026-01-02",
"descripcion":"Transferencia recibida",
"comercio":None,
"moneda":"ARS",
"monto":850000,
"movimiento":"CREDITO"
},

{
"id":2,
"cliente_id":1,
"cuenta_id":5001,
"tipo":"CUENTA",
"categoria":"PAGO",
"fecha":"2026-01-05",
"descripcion":"Pago supermercado",
"comercio":"Carrefour",
"moneda":"ARS",
"monto":-45000,
"movimiento":"DEBITO"
},

{
"id":3,
"cliente_id":1,
"cuenta_id":5001,
"tipo":"CUENTA",
"categoria":"SERVICIO",
"fecha":"2026-01-10",
"descripcion":"Pago electricidad",
"comercio":"Edenor",
"moneda":"ARS",
"monto":-18000,
"movimiento":"DEBITO"
},



# ==========================
# CUENTA 5002 DOLARES
# ==========================

{
"id":10,
"cliente_id":1,
"cuenta_id":5002,
"tipo":"CUENTA",
"categoria":"TRANSFERENCIA",
"fecha":"2026-01-05",
"descripcion":"Transferencia exterior",
"comercio":None,
"moneda":"USD",
"monto":2500,
"movimiento":"CREDITO"
},


{
"id":11,
"cliente_id":1,
"cuenta_id":5002,
"tipo":"CUENTA",
"categoria":"COMPRA",
"fecha":"2026-01-20",
"descripcion":"Compra dólares",
"comercio":None,
"moneda":"USD",
"monto":-500,
"movimiento":"DEBITO"
},



# ==========================
# CUENTA 5003 EUROS
# ==========================

{
"id":20,
"cliente_id":1,
"cuenta_id":5003,
"tipo":"CUENTA",
"categoria":"TRANSFERENCIA",
"fecha":"2026-01-08",
"descripcion":"Transferencia recibida",
"comercio":None,
"moneda":"EUR",
"monto":1500,
"movimiento":"CREDITO"
},


{
"id":21,
"cliente_id":1,
"cuenta_id":5003,
"tipo":"CUENTA",
"categoria":"SERVICIO",
"fecha":"2026-01-25",
"descripcion":"Pago servicio internacional",
"comercio":"Netflix",
"moneda":"EUR",
"monto":-200,
"movimiento":"DEBITO"
},




# ==========================
# CUENTA CORRIENTE 5004
# ==========================

{
"id":30,
"cliente_id":1,
"cuenta_id":5004,
"tipo":"CUENTA",
"categoria":"DEPOSITO",
"fecha":"2026-01-03",
"descripcion":"Deposito cuenta corriente",
"comercio":None,
"moneda":"ARS",
"monto":300000,
"movimiento":"CREDITO"
},


{
"id":31,
"cliente_id":1,
"cuenta_id":5004,
"tipo":"CUENTA",
"categoria":"PAGO",
"fecha":"2026-01-18",
"descripcion":"Pago proveedor",
"comercio":"Proveedor SA",
"moneda":"ARS",
"monto":-70000,
"movimiento":"DEBITO"
},




# =====================================================
# VISA SIGNATURE 101 - TARJETA CREDITO
# =====================================================


{
"id":100,
"cliente_id":1,
"tarjeta_id":101,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-01-03",
"descripcion":"Carga combustible",
"comercio":"YPF",
"moneda":"ARS",
"monto":-45000,
"movimiento":"DEBITO",
"cuotas":{
    "actual":1,
    "total":1
}
},



{
"id":101,
"cliente_id":1,
"tarjeta_id":101,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-01-06",
"descripcion":"Compra Amazon",
"comercio":"Amazon",
"moneda":"USD",
"monto":-120,
"movimiento":"DEBITO",
"cuotas":{
    "actual":1,
    "total":1
}
},



{
"id":102,
"cliente_id":1,
"tarjeta_id":101,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-01-12",
"descripcion":"Compra tecnologia",
"comercio":"Mercado Libre",
"moneda":"ARS",
"monto":-250000,
"movimiento":"DEBITO",
"cuotas":{
    "actual":1,
    "total":6
}
},

{
"id":103,
"cliente_id":1,
"tarjeta_id":101,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-01-13",
"descripcion":"Compra Amazon",
"comercio":"Amazon",
"moneda":"USD",
"monto":-4120,
"movimiento":"DEBITO",
"cuotas":{
    "actual":1,
    "total":1
}
},


{
"id":104,
"cliente_id":1,
"tarjeta_id":101,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-01-15",
"descripcion":"Compra tecnologia",
"comercio":"Mercado Libre",
"moneda":"ARS",
"monto":-450000,
"movimiento":"DEBITO",
"cuotas":{
    "actual":3,
    "total":12
}
},

# =====================================================
# MASTERCARD BLACK 102 - TARJETA CREDITO
# =====================================================


{
"id":200,
"cliente_id":1,
"tarjeta_id":102,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-01-04",
"descripcion":"Compra indumentaria",
"comercio":"Zara",
"moneda":"ARS",
"monto":-30000,
"movimiento":"DEBITO",
"cuotas":{
    "actual":1,
    "total":3
}
},





# =====================================================
# VISA DEBITO 103
# =====================================================


{
"id":300,
"cliente_id":1,
"tarjeta_id":103,
"tipo":"TARJETA_DEBITO",
"categoria":"COMPRA",
"fecha":"2026-01-15",
"descripcion":"Compra farmacia",
"comercio":"Farmacity",
"moneda":"ARS",
"monto":-8000,
"movimiento":"DEBITO"
},




# =====================================================
# CLIENTE 2 - MARIA
# =====================================================


{
"id":600,
"cliente_id":2,
"cuenta_id":6001,
"tipo":"CUENTA",
"categoria":"TRANSFERENCIA",
"fecha":"2026-01-05",
"descripcion":"Sueldo recibido",
"comercio":None,
"moneda":"ARS",
"monto":500000,
"movimiento":"CREDITO"
},



{
"id":601,
"cliente_id":2,
"tarjeta_id":201,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-01-12",
"descripcion":"Compra ropa",
"comercio":"Mimo",
"moneda":"ARS",
"monto":-35000,
"movimiento":"DEBITO",
"cuotas":{
    "actual":1,
    "total":2
}
},




# =====================================================
# CLIENTE 3 - ROCIO
# =====================================================


{
"id":900,
"cliente_id":3,
"cuenta_id":7001,
"tipo":"CUENTA",
"categoria":"DEPOSITO",
"fecha":"2026-01-03",
"descripcion":"Deposito efectivo",
"comercio":None,
"moneda":"ARS",
"monto":80000,
"movimiento":"CREDITO"
},



{
"id":901,
"cliente_id":3,
"tarjeta_id":301,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-01-04",
"descripcion":"Compra farmacia",
"comercio":"Farmacia",
"moneda":"ARS",
"monto":-8000,
"movimiento":"DEBITO",
"cuotas":{
    "actual":1,
    "total":1
}
},

# Movimientos adicionales para perfiles de prueba
{

"id":1000,
"cliente_id":5,
"cuenta_id":8001,
"tipo":"CUENTA",
"categoria":"DEPOSITO",
"fecha":"2026-02-01",
"descripcion":"Deposito inicial",
"comercio":None,
"moneda":"ARS",
"monto":20000,
"movimiento":"CREDITO"
},
{
"id":1001,
"cliente_id":5,
"tarjeta_id":401,
"tipo":"TARJETA_DEBITO",
"categoria":"COMPRA",
"fecha":"2026-02-05",
"descripcion":"Compra supermercado",
"comercio":"Dia",
"moneda":"ARS",
"monto":-1500,
"movimiento":"DEBITO"
},

{
"id":1002,
"cliente_id":6,
"cuenta_id":8002,
"tipo":"CUENTA",
"categoria":"TRANSFERENCIA",
"fecha":"2026-03-01",
"descripcion":"Sueldo recibido",
"comercio":None,
"moneda":"ARS",
"monto":150000,
"movimiento":"CREDITO"
},
{
"id":1003,
"cliente_id":6,
"tarjeta_id":402,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-03-05",
"descripcion":"Compra online",
"comercio":"Mercado Libre",
"moneda":"ARS",
"monto":-4500,
"movimiento":"DEBITO",
"cuotas":{"actual":1,"total":1}
},

{
"id":1004,
"cliente_id":7,
"cuenta_id":8003,
"tipo":"CUENTA",
"categoria":"TRANSFERENCIA",
"fecha":"2026-04-01",
"descripcion":"Transferencia recibida",
"comercio":None,
"moneda":"ARS",
"monto":500000,
"movimiento":"CREDITO"
},
{
"id":1005,
"cliente_id":7,
"tarjeta_id":403,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-04-10",
"descripcion":"Compra tecnologia",
"comercio":"CompuStore",
"moneda":"ARS",
"monto":-80000,
"movimiento":"DEBITO",
"cuotas":{"actual":1,"total":6}
},

{
"id":1006,
"cliente_id":8,
"cuenta_id":8005,
"tipo":"CUENTA",
"categoria":"TRANSFERENCIA",
"fecha":"2026-05-01",
"descripcion":"Transferencia internacional",
"comercio":None,
"moneda":"USD",
"monto":10000,
"movimiento":"CREDITO"
},
{
"id":1007,
"cliente_id":8,
"cuenta_id":8006,
"tipo":"CUENTA",
"categoria":"COMPRA",
"fecha":"2026-05-03",
"descripcion":"Compra en el exterior",
"comercio":"Airbnb",
"moneda":"USD",
"monto":-250,
"movimiento":"DEBITO"
},

{
"id":1008,
"cliente_id":9,
"cuenta_id":8007,
"tipo":"CUENTA",
"categoria":"DEPOSITO",
"fecha":"2026-01-10",
"descripcion":"Depósito comercial",
"comercio":None,
"moneda":"ARS",
"monto":900000,
"movimiento":"CREDITO"
},
{
"id":1009,
"cliente_id":9,
"tarjeta_id":406,
"tipo":"TARJETA_CREDITO",
"categoria":"COMPRA",
"fecha":"2026-01-15",
"descripcion":"Compra internacional",
"comercio":"Louis Vuitton",
"moneda":"EUR",
"monto":-2500,
"movimiento":"DEBITO",
"cuotas":{"actual":1,"total":3}
},

{
"id":1010,
"cliente_id":10,
"cuenta_id":8009,
"tipo":"CUENTA",
"categoria":"DEPOSITO",
"fecha":"2026-02-01",
"descripcion":"Pago cliente X",
"comercio":None,
"moneda":"ARS",
"monto":2000000,
"movimiento":"CREDITO"
},
{
"id":1011,
"cliente_id":10,
"cuenta_id":8009,
"tipo":"CUENTA",
"categoria":"PAGO",
"fecha":"2026-02-05",
"descripcion":"Pago a proveedor",
"comercio":"Proveedor SA",
"moneda":"ARS",
"monto":-150000,
"movimiento":"DEBITO"
},

{
"id":1012,
"cliente_id":11,
"cuenta_id":8101,
"tipo":"CUENTA",
"categoria":"INFO",
"fecha":"2026-01-01",
"descripcion":"Cuenta creada - sin movimientos",
"comercio":None,
"moneda":"ARS",
"monto":0,
"movimiento":"CREDITO"
},

{
"id":1013,
"cliente_id":13,
"cuenta_id":8301,
"tipo":"CUENTA",
"categoria":"DEPOSITO",
"fecha":"2026-03-01",
"descripcion":"Depósito inicial",
"comercio":None,
"moneda":"ARS",
"monto":50000,
"movimiento":"CREDITO"
},

{
"id":1014,
"cliente_id":14,
"cuenta_id":8401,
"tipo":"CUENTA",
"categoria":"TRANSFERENCIA",
"fecha":"2026-04-01",
"descripcion":"Transferencia recibida",
"comercio":None,
"moneda":"ARS",
"monto":200000,
"movimiento":"CREDITO"
},

{
"id":1015,
"cliente_id":14,
"cuenta_id":8402,
"tipo":"CUENTA",
"categoria":"TRANSFERENCIA",
"fecha":"2026-04-02",
"descripcion":"Transferencia USD",
"comercio":None,
"moneda":"USD",
"monto":5000,
"movimiento":"CREDITO"
},

# =====================================================
# BLOQUE: CLIENTE 12 - MUCHOS MOVIMIENTOS (200+)
# =====================================================
]

# Generar 205 movimientos adicionales para el cliente_id 12 (cuenta 8201)
for _i in range(1100, 1305):
    idx = _i - 1100
    mes = (idx // 28) % 12 + 1
    dia = (idx % 28) + 1
    fecha = f"2025-{mes:02d}-{dia:02d}"
    monto = -((idx % 5) + 1) * 1000 if _i % 2 == 0 else ((idx % 4) + 1) * 1500
    movimiento_tipo = "DEBITO" if monto < 0 else "CREDITO"
    categoria = "PAGO" if _i % 3 == 0 else ("DEPOSITO" if _i % 5 == 0 else "TRANSFERENCIA")
    movimientos.append({
        "id": _i,
        "cliente_id": 12,
        "cuenta_id": 8201,
        "tipo": "CUENTA",
        "categoria": categoria,
        "fecha": fecha,
        "descripcion": f"Movimiento masivo { _i }",
        "comercio": None,
        "moneda": "ARS",
        "monto": monto,
        "movimiento": movimiento_tipo
    })

