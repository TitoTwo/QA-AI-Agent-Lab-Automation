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
    "total":3
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
}

]