from herramientas.llm import consultar_llm

def generar_gherkin(historia):

    prompt = f"""
    Actúa como un QA Senior.

    Genera casos Gherkin.

    Historia:

    {historia}
    """

    return consultar_llm(prompt)