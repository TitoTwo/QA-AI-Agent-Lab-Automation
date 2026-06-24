from herramientas.registry import HERRAMIENTAS
from herramientas.archivos import guardar_archivo


def ejecutar_plan(
    plan,
    historia,
    nombre,
    resultados_dir
):

    # Crear carpeta de la historia

    historia_dir = resultados_dir / nombre

    historia_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    for tarea in plan.splitlines():

        tarea = tarea.strip()

        if not tarea:
            continue

        if tarea not in HERRAMIENTAS:

            print(f"Tarea desconocida: {tarea}")

            continue

        print(f"Ejecutando {tarea}...")

        funcion = HERRAMIENTAS[tarea]

        resultado = funcion(historia)

        if tarea == "GENERAR_GHERKIN":

            guardar_archivo(
                historia_dir / f"{nombre}.feature",
                resultado
            )

        elif tarea == "GENERAR_DATOS":

            guardar_archivo(
                historia_dir / f"{nombre}_datos.csv",
                resultado
            )

        elif tarea == "GENERAR_RIESGOS":

            guardar_archivo(
                historia_dir / f"{nombre}_riesgos.txt",
                resultado
            )

        elif tarea == "GENERAR_CASOS_NEGATIVOS":

            guardar_archivo(
                historia_dir / f"{nombre}_casos_negativos.txt",
                resultado
            )

        elif tarea == "GENERAR_CRITERIOS_ACEPTACION":

            guardar_archivo(
                historia_dir / f"{nombre}_criterios.txt",
                resultado
            )
        elif tarea == "GENERAR_CASOS_API":

            guardar_archivo(
                historia_dir / f"{nombre}_api.txt",
                resultado
            )