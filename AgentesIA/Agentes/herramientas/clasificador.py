# Se crea este archivo porque el modelo que usamos es muy pequeño (llm)
from herramientas.llm import consultar_llm


def clasificar_historia(historia):

    prompt = f"""
Eres un QA Lead Senior especializado en sistemas bancarios.

Debes clasificar la siguiente historia en una única categoría:

SIMPLE
MEDIA
COMPLEJA

Definiciones:

SIMPLE:
- Actualización de datos
- Consultas
- Cambios visuales

MEDIA:
- Reposición de tarjetas
- Gestión de productos
- Validaciones de negocio

COMPLEJA:
- Financiamiento
- Cuotas
- Pagos
- Débitos automáticos
- Cálculos financieros
- Reglas de negocio complejas

IMPORTANTE:

Responde únicamente con una palabra:

SIMPLE

o

MEDIA

o

COMPLEJA

Historia:

{historia}
"""

    respuesta = consultar_llm(prompt)

    respuesta = (
        respuesta
        .strip()
        .upper()
        .replace(".", "")
        .replace(":", "")
        .replace("-", "")
    )

    if "COMPLEJ" in respuesta:
        return "COMPLEJA"

    if "MEDI" in respuesta:
        return "MEDIA"

    if "SIMPL" in respuesta:
        return "SIMPLE"

    print(
        f"Advertencia: clasificación desconocida '{respuesta}'. "
        "Se utilizará MEDIA."
    )

    return "MEDIA"