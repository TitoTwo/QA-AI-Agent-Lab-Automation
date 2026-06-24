from herramientas.llm import consultar_llm


def generar_casos_api(historia):

    prompt = f"""
Eres un QA Backend Senior especializado en APIs bancarias.

Basándote únicamente en la historia proporcionada:

Genera:

- Endpoint sugerido
- Método HTTP
- 3 casos positivos
- 3 casos negativos

Para cada caso incluir:

Caso:
Request:
Resultado esperado:

Utiliza formato JSON para los request.

Historia:

{historia}
"""

    return consultar_llm(prompt)