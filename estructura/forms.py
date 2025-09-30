from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, time

from .models import Cliente, Reserva, Venta, Paquete
import datetime

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ClienteRegistrationForm(UserCreationForm):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Cliente.objects.create(
                user=user,
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
                email=self.cleaned_data['email'],
                telefono=self.cleaned_data['telefono'],
                direccion=self.cleaned_data['direccion']
            )
        return user


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha', 'hora', 'cliente_nombre', 'cliente_email', 'paquete', 'servicio']
        widgets = {
            'fecha': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'min': date.today().isoformat(),
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control',
                    'min': time(8,0).strftime('%H:%M'),
                    'max': time(16,0).strftime('%H:%M'),
                    'step': 1800,
                }
            ),
            'cliente_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'paquete': forms.Select(attrs={'class': 'form-select'}),
            'servicio': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if Reserva.objects.filter(fecha=fecha).count() >= 3:
            raise ValidationError("Este día ya tiene 3 eventos, elige otra fecha.")
        return fecha

    def clean_hora(self):
        hora = self.cleaned_data['hora']
        if hora < time(8, 0) or hora > time(16, 0):
            raise ValidationError("La hora debe estar entre 08:00 y 16:00")
        return hora

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['paquete']
    

class ClienteUpdateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']  # Asegúrate de que los campos coincidan con tu modelo
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }

