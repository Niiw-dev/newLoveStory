from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, time
from django.utils import timezone
from datetime import datetime
from pytz import timezone as pytz_timezone

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
    # Campos extra solo si el usuario NO está logueado
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Reserva
        fields = ['fecha', 'hora', 'paquete', 'servicio']
        widgets = {
            'fecha': forms.HiddenInput(),
            'hora': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'type': 'time',
                    'class': 'form-control',
                    'step': 60,
                    'onclick': "this.showPicker();"
                }
            ),
            'paquete': forms.Select(attrs={'class': 'form-select'}),
            'servicio': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        hora = cleaned_data.get('hora')
        paquete = cleaned_data.get('paquete')

        if not fecha or not hora or not paquete:
            return cleaned_data

        # Duración del paquete + 1 hora extra
        duracion_total_minutos = paquete.duracion + 60
        nueva_reserva_inicio = datetime.datetime.combine(fecha, hora)
        nueva_reserva_fin = nueva_reserva_inicio + datetime.timedelta(minutes=duracion_total_minutos)

        # Revisar todas las reservas existentes ese día
        reservas_dia = Reserva.objects.filter(fecha=fecha)
        for r in reservas_dia:
            inicio = datetime.datetime.combine(r.fecha, r.hora)
            fin = inicio + datetime.timedelta(minutes=r.paquete.duracion + 60)

            # Validación de solapamiento
            if (nueva_reserva_inicio < fin) and (nueva_reserva_fin > inicio):
                raise forms.ValidationError(
                    f"No se puede agendar en ese horario. Ocupado desde {inicio.time().strftime('%H:%M')} hasta {fin.time().strftime('%H:%M')}."
                )

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        bogota = pytz_timezone('America/Bogota')
        ahora_bogota = timezone.now().astimezone(bogota).time()
        if not self.instance.pk:
            self.initial['hora'] = ahora_bogota

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

