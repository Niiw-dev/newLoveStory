from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from estructura.models import Reserva

class Command(BaseCommand):
    help = "Cancela reservas pendientes que pasaron 48 horas"

    def handle(self, *args, **kwargs):
        ahora = timezone.now().replace(microsecond=0)
        limite = ahora - timedelta(hours=48)

        pendientes = Reserva.objects.filter(estado="pendiente", creado_en__lt=limite)
        total = pendientes.count()

        for reserva in pendientes:
            reserva.estado = "cancelada"
            reserva.save()
            self.stdout.write(self.style.SUCCESS(f"Reserva {reserva.payment_reference} cancelada automáticamente"))

        self.stdout.write(self.style.SUCCESS(f"Total de reservas canceladas: {total}"))
