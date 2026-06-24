from herramientas.clasificador import clasificar_historia


def generar_plan(historia):

    clasificacion = clasificar_historia(historia)

    print(f"Clasificación detectada: {clasificacion}")

    if "SIMPLE" in clasificacion:

        return """
GENERAR_GHERKIN
"""

    elif "MEDIA" in clasificacion:

        return """
GENERAR_GHERKIN
GENERAR_DATOS
GENERAR_CRITERIOS_ACEPTACION
"""

    elif "COMPLEJA" in clasificacion:

        return """
GENERAR_GHERKIN
GENERAR_DATOS
GENERAR_RIESGOS
GENERAR_CASOS_NEGATIVOS
GENERAR_CRITERIOS_ACEPTACION
GENERAR_CASOS_API
GENERAR_TEST_PYTEST
"""

    return """
GENERAR_GHERKIN
"""