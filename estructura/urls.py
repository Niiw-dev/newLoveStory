from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('acerca_de_nosotros/', views.acerca_de_nosotros, name='acerca_de_nosotros'),
    path('', views.inicio, name='inicio'),
    path('reservas/', views.reservas, name='reservas'),
    path('api/hacer-reserva/', views.hacer_reserva, name='hacer_reserva'),
    path('api/obtener-reservas/', views.obtener_reservas, name='obtener_reservas'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registrate/', views.register, name='registrate'),
    path('ideas/', views.ideas, name='ideas'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('paquetes/', views.paquetes, name='paquetes'),
]