from herramientas.llm import consultar_llm

def generar_datos_prueba(historia):

    prompt = f"""
    Genera datos de prueba en formato CSV.

    Historia:

    {historia}
    """

    return consultar_llm(prompt)