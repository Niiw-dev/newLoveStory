from django.db import migrations

def crear_paquetes_y_servicios(apps, schema_editor):
    Servicio = apps.get_model("estructura", "Servicio")
    Paquete = apps.get_model("estructura", "Paquete")

    # Servicios
    servicios = [
        {"tipo_de_servicio": "Fotografía de boda", "descripcion": "Cobertura completa de boda", "precio_base": 1500.00, "duracion": 240, "categoria": "boda"},
        {"tipo_de_servicio": "Sesión de retrato", "descripcion": "Sesión individual en estudio o exterior", "precio_base": 200.00, "duracion": 60, "categoria": "retrato"},
        {"tipo_de_servicio": "Fotografía empresarial", "descripcion": "Cobertura de eventos y fotos corporativas", "precio_base": 800.00, "duracion": 180, "categoria": "empresarial"},
    ]
    for s in servicios:
        Servicio.objects.create(**s)

    # Paquetes
    paquetes = [
        {"nombre_paquete": "Paquete Básico", "descripcion": "Incluye sesión de 1 hora y 20 fotos editadas", "precio": 250.00, "duracion": 60},
        {"nombre_paquete": "Paquete Premium", "descripcion": "Incluye 4 horas de sesión, 100 fotos editadas y álbum impreso", "precio": 1200.00, "duracion": 240},
        {"nombre_paquete": "Paquete Empresarial", "descripcion": "Cobertura de evento corporativo de 3 horas", "precio": 900.00, "duracion": 180},
    ]
    for p in paquetes:
        Paquete.objects.create(**p)


def borrar_paquetes_y_servicios(apps, schema_editor):
    Servicio = apps.get_model("estructura", "Servicio")
    Paquete = apps.get_model("estructura", "Paquete")
    Servicio.objects.all().delete()
    Paquete.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("estructura", "0001_initial"),  # cámbiala al número correcto
    ]

    operations = [
        migrations.RunPython(crear_paquetes_y_servicios, borrar_paquetes_y_servicios),
    ]
