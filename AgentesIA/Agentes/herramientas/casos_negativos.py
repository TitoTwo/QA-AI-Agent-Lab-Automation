from herramientas.llm import consultar_llm


def generar_casos_negativos(historia):

    prompt = f"""
Eres un QA Senior especializado en testing funcional y bancario.

Genera exactamente 5 casos de prueba negativos.

Utiliza únicamente información presente en la historia.

No inventes funcionalidades.

Considera:

- Campos obligatorios
- Valores inválidos
- Valores fuera de rango
- Reglas de negocio
- Errores de integración

Cada caso debe contener:

Caso:
Resultado esperado:

Los escenarios deben ser realistas y útiles para pruebas.

Formato:

Caso 1:
Resultado esperado:

Caso 2:
Resultado esperado:

Caso 3:
Resultado esperado:

Caso 4:
Resultado esperado:

Caso 5:
Resultado esperado:

Historia:

{historia}
"""

    return consultar_llm(prompt)