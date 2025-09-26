from django.db import models
from django.contrib.auth.models import User
from datetime import time, date
from django.core.exceptions import ValidationError

class Servicio(models.Model):
    tipo_de_servicio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tipo_de_servicio

class Paquete(models.Model):
    nombre_paquete = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_paquete

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Reserva(models.Model):
    TIPO_EVENTO_CHOICES = [
        ('boda', 'Boda'),
        ('quince', 'Quinceañera'),
        ('bautizo', 'Bautizo'),
        ('comunion', 'Primera Comunión'),
        ('graduacion', 'Graduación'),
        ('cumpleanos', 'Cumpleaños'),
        ('empresarial', 'Evento Empresarial'),
        ('otros', 'Otros'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    tipo_evento = models.CharField(max_length=20, choices=TIPO_EVENTO_CHOICES)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ], default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        # Validar que no haya más de 3 reservas confirmadas para la misma fecha
        if self.fecha:
            reservas_del_dia = Reserva.objects.filter(
                fecha=self.fecha,
                estado__in=['pendiente', 'confirmada']
            ).exclude(id=self.id if self.id else None)
            
            if reservas_del_dia.count() >= 3:
                raise ValidationError('Ya existen 3 reservas para esta fecha. Por favor selecciona otra fecha.')
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente} - {self.fecha}"

# Tus otros modelos permanecen igual...
class Venta(models.Model):
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente}"

class Foto(models.Model):
    url = models.URLField(max_length=255)
    descripcion = models.CharField(max_length=50)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class EventoFotografico(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=200)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class ImagenEvento(models.Model):
    evento = models.ForeignKey(EventoFotografico, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='eventos/')
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Imagen de {self.evento.titulo}"
