from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import guardar_reserva_ajax



urlpatterns = [
    path('acerca_de_nosotros/', views.acerca_de_nosotros, name='acerca_de_nosotros'),
    path('', views.inicio, name='inicio'),
    path('reserva/', views.agendar_reserva, name='agendar_reserva'),
    path('reserva_exitosa/', views.reserva_exitosa, name='reserva_exitosa'),  # página de confirmación
    path('api/obtener-reservas/', views.obtener_reservas, name='obtener_reservas'),
    path('api/paquetes/', views.obtener_paquetes, name='obtener_paquetes'),
    path('login_view', views.login_view, name='login_view'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registrate/', views.register, name='registrate'),
    path('ideas/', views.ideas, name='ideas'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('paquetes/', views.paquetes, name='paquetes'),
    path('api/horas-disponibles/', views.horas_disponibles, name='horas_disponibles'),
    path('guardar_reserva/', views.guardar_reserva_ajax, name='guardar_reserva_ajax'),
   
]
