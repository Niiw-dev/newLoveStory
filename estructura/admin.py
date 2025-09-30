from django.contrib import admin
from .models import Paquete, Reserva, Cliente, Servicio

@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('nombre_paquete', 'descripcion', 'precio')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'cliente_nombre', 'estado', 'paquete', 'servicio')
    list_filter = ('fecha', 'estado', 'paquete', 'servicio')
    search_fields = ('cliente_nombre', 'cliente_email')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('tipo_de_servicio', 'descripcion', 'precio_base')
