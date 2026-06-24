from herramientas.gherkin import generar_gherkin
from herramientas.datos_prueba import generar_datos_prueba
from herramientas.riesgos import generar_riesgos
from herramientas.casos_negativos import generar_casos_negativos
from herramientas.criterios_aceptacion import generar_criterios_aceptacion
from herramientas.casos_api import generar_casos_api


HERRAMIENTAS = {
    "GENERAR_GHERKIN": generar_gherkin,
    "GENERAR_DATOS": generar_datos_prueba,
    "GENERAR_RIESGOS": generar_riesgos,
    "GENERAR_CASOS_NEGATIVOS": generar_casos_negativos,
    "GENERAR_CRITERIOS_ACEPTACION": generar_criterios_aceptacion,
    "GENERAR_CASOS_API": generar_casos_api
}