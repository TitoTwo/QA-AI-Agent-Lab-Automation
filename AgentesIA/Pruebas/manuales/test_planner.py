from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR / "Agentes"))

from herramientas.planner import generar_plan

historia = """
Como cliente quiero financiar mi saldo
para pagarlo en cuotas.
"""

plan = generar_plan(historia)

print(plan)