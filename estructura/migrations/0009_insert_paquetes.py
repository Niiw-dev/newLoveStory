from django.db import migrations
from datetime import timedelta

def crear_paquetes_iniciales(apps, schema_editor):
    Paquete = apps.get_model('estructura', 'Paquete')
    Paquete.objects.bulk_create([
        Paquete(
            nombre_paquete="Básico",
            descripcion="Sesión de 1 hora, 20 fotos editadas en digital.",
            precio=300000,
            duracion=timedelta(hours=1)  # <-- aquí usamos timedelta
        ),
        Paquete(
            nombre_paquete="Premium",
            descripcion="Sesión de 3 horas, 50 fotos editadas + álbum digital.",
            precio=700000,
            duracion=timedelta(hours=3)
        ),
        Paquete(
            nombre_paquete="Full Day",
            descripcion="Cobertura completa de evento, fotos ilimitadas + video resumen.",
            precio=1500000,
            duracion=timedelta(hours=8)
        ),
    ])

def eliminar_paquetes_iniciales(apps, schema_editor):
    Paquete = apps.get_model('estructura', 'Paquete')
    Paquete.objects.filter(nombre_paquete__in=["Básico", "Premium", "Full Day"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0008_paquete_duracion'),
    ]

    operations = [
        migrations.RunPython(crear_paquetes_iniciales, eliminar_paquetes_iniciales),
    ]
