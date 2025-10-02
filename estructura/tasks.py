import threading
from django.core.management import call_command

def run_cancelar_reservas():
    # Ejecuta tu comando Django
    call_command('cancelar_reservas')

    # Vuelve a programarlo en 48 horas (48*60*60 segundos)
    threading.Timer(48*60*60, run_cancelar_reservas).start()
