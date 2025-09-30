from django.db import migrations
from datetime import timedelta

def crear_servicios_iniciales(apps, schema_editor):
    Servicio = apps.get_model('estructura', 'Servicio')
    Servicio.objects.bulk_create([
        Servicio(
            tipo_de_servicio="Sesión Retrato",
            descripcion="Sesión de 1 hora para retratos individuales o familiares.",
            precio_base=250000,
            duracion=timedelta(hours=1),
            categoria="retrato"
        ),
        Servicio(
            tipo_de_servicio="Cobertura Boda",
            descripcion="Cobertura completa de ceremonia y fiesta.",
            precio_base=1500000,
            duracion=timedelta(hours=8),
            categoria="boda"
        ),
        Servicio(
            tipo_de_servicio="Fotografía Empresarial",
            descripcion="Sesión para fotos de productos o corporativas.",
            precio_base=500000,
            duracion=timedelta(hours=3),
            categoria="empresarial"
        ),
    ])

def eliminar_servicios_iniciales(apps, schema_editor):
    Servicio = apps.get_model('estructura', 'Servicio')
    Servicio.objects.filter(tipo_de_servicio__in=[
        "Sesión Retrato", "Cobertura Boda", "Fotografía Empresarial"
    ]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0010_servicio_categoria_servicio_duracion_and_more'),  # cambiar según la última migración aplicada
    ]

    operations = [
        migrations.RunPython(crear_servicios_iniciales, eliminar_servicios_iniciales),
    ]
