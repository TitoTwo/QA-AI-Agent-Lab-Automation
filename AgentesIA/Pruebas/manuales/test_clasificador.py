from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR / "Agentes"))

from herramientas.clasificador import clasificar_historia


historias = [
    (
        "Simple",
        """
        Como usuario quiero actualizar mi dirección de correo electrónico
        para recibir notificaciones en una nueva casilla.
        """
    ),
    (
        "Media",
        """
        Como cliente quiero solicitar la reposición de mi tarjeta de crédito
        para continuar operando cuando la tarjeta actual esté dañada.
        """
    ),
    (
        "Compleja",
        """
        Como cliente quiero financiar el saldo de mi tarjeta de crédito
        en hasta 24 cuotas para poder pagar mi deuda en forma financiada.
        """
    ),
    (
        "Debito",
        """
        Como cliente quiero adherir mi tarjeta de crédito al débito automático
        para que el pago mensual se debite automáticamente de mi cuenta bancaria.
        """
    )
]

for nombre, historia in historias:

    resultado = clasificar_historia(historia)

    print(f"\nHistoria: {nombre}")
    print(f"Clasificación: {resultado}")