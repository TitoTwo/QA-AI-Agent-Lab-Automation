from herramientas.llm import consultar_llm


def generar_criterios_aceptacion(historia):

    prompt = f"""
Eres un QA Senior especializado en análisis funcional.

Debes generar criterios de aceptación utilizando
ÚNICAMENTE la información presente en la historia.

Reglas obligatorias:

- No inventes funcionalidades.
- No agregues pantallas.
- No agregues notificaciones.
- No agregues correos electrónicos.
- No agregues reportes.
- No agregues procesos adicionales.
- Si una funcionalidad no está mencionada en la historia, no debe aparecer.

Los criterios deben:

- Ser claros.
- Ser verificables.
- Estar orientados a pruebas funcionales.
- Tener relación directa con la historia.

Genera entre 3 y 8 criterios.

Formato:

Criterio 1:
...

Criterio 2:
...

Criterio 3:
...

Historia:

{historia}
"""

    return consultar_llm(prompt)