from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ClienteRegistrationForm
from .forms import ClienteUpdateForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reserva, Cliente, Servicio, Paquete
import json
from datetime import datetime, time
from .models import EventoFotografico


def paquetes(request):
    return render(request, 'paginas/servicios/paquetes.html')

# Vista para la página "Acerca de Nosotros"
def acerca_de_nosotros(request):
    return render(request, 'paginas/nosotros/acerca_de_nosotros.html')

# Vista para la página de inicio
def inicio(request):
    return render(request, 'paginas/inicio/inicio.html')

# Vista para las reservas
@login_required(login_url='/login/')
def reservas(request):
    return render(request, 'paginas/servicios/reservas.html')

# Vista de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reservas')  # Redirige a la página de reservas después de iniciar sesión
        else:
            # Mensaje de error si las credenciales no son correctas
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    # Mensaje de advertencia si el usuario fue redirigido a la página de inicio de sesión
    if not request.user.is_authenticated:
        messages.warning(request, 'Debes iniciar sesión para hacer una reserva.')

    return render(request, 'login.html')

# Vista para la página de registro

def ideas(request):
    return render(request, 'paginas/servicios/ideas.html')

def register(request):
    if request.method == 'POST':
        form = ClienteRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = ClienteRegistrationForm()
    return render(request, 'registrate.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def perfil_usuario(request):
    """
    Vista para mostrar y actualizar el perfil del usuario.
    """
    try:
        # Obtener el cliente asociado al usuario actual
        cliente = request.user.cliente
        user = request.user  # El usuario actualmente autenticado
    except cliente.DoesNotExist:
        return redirect('registrate')

    if request.method == 'POST':
        form = ClienteUpdateForm(request.POST, instance=cliente)
        if form.is_valid():
            # Guardar los cambios en los campos del cliente
            cliente = form.save(commit=False)
            # Verificar si se ha cambiado el username
            nuevo_username = form.cleaned_data.get('username')
            if nuevo_username and nuevo_username != user.username:
                user.username = nuevo_username
                user.save()
            cliente.save()
            messages.success(request, 'Tu perfil ha sido actualizado con éxito.')
        else:
            messages.error(request, 'Hubo un error al actualizar tu perfil. Por favor, revisa los datos.')
    else:
        form = ClienteUpdateForm(instance=cliente)

    context = {
        'cliente': cliente,
        'form': form
    }
    return render(request, 'perfil_usuario.html', context)
def pagina_reservas(request):
    servicios = Servicio.objects.all()
    horas_disponibles = [time(hour=h).strftime("%H:%M") for h in range(9, 21)]
    return render(request, 'reservas.html', {
        'servicios': servicios,
        'horas_disponibles': horas_disponibles
    })

@csrf_exempt
def hacer_reserva(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            fecha_hora = datetime.strptime(f"{data['fecha']} {data['hora']}", "%Y-%m-%d %H:%M")
            
            # Verificar si el cliente está autenticado
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Debes iniciar sesión para hacer una reserva'}, status=401)

            # Obtener el cliente autenticado
            cliente = request.user.cliente
            
            # Obtener el servicio a partir del ID
            servicio_id = data.get('servicio')
            try:
                servicio = Servicio.objects.get(id=servicio_id)
            except Servicio.DoesNotExist:
                return JsonResponse({'error': 'Servicio no encontrado'}, status=404)

            # Verificar si ya existe una reserva para esa fecha, hora y servicio
            if Reserva.objects.filter(fecha_reserva=fecha_hora, servicio=servicio).exists():
                return JsonResponse({'error': 'Ya existe una reserva para esta fecha, hora y servicio'}, status=400)

            # Crear nueva reserva
            nueva_reserva = Reserva.objects.create(
                fecha_reserva=fecha_hora,
                cliente=cliente,
                servicio=servicio
            )

            return JsonResponse({'mensaje': 'Reserva creada con éxito'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def obtener_reservas(request):
    reservas = Reserva.objects.all()
    eventos = [{
        'title': f"{reserva.servicio.tipo_de_servicio} - {reserva.cliente.nombre}",
        'start': reserva.fecha_reserva.isoformat(),
        'extendedProps': {
            'estado': reserva.estado
        }
    } for reserva in reservas]
    return JsonResponse(eventos, safe=False)

