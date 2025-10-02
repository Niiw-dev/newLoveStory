from django.apps import AppConfig

class EstructuraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estructura'

    def ready(self):
        from .tasks import run_cancelar_reservas
#        run_cancelar_reservas()
