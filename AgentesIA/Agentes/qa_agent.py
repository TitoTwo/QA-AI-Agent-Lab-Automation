from pathlib import Path

from herramientas.planner import generar_plan
from herramientas.executor import ejecutar_plan


BASE_DIR = Path(__file__).resolve().parent.parent

historias_dir = BASE_DIR / "Historias"
resultados_dir = BASE_DIR / "Resultados"
processed = set()


for historia_file in historias_dir.glob("*.txt"):

    print(f"\nProcesando: {historia_file.name}")

    with open(historia_file, "r", encoding="utf-8") as archivo:
        historia = archivo.read()

    nombre = historia_file.stem

    plan = generar_plan(historia)

    print("\nPLAN:")
    print(plan)

    ejecutar_plan(
        plan,
        historia,
        nombre,
        resultados_dir
    )

    if nombre not in processed:
        print(f"Finalizado: {nombre}")
        processed.add(nombre)

print("\nProceso completado.")