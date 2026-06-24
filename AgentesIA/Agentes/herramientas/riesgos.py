from herramientas.llm import consultar_llm

def generar_riesgos(historia):

    prompt = f"""
    Identifica riesgos funcionales,
    técnicos y casos borde.

    Historia:

    {historia}
    """

    return consultar_llm(prompt)