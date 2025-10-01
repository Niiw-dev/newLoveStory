import calendar

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
import json
from datetime import date, time
from django.utils import timezone
from .models import Cliente, Paquete, Reserva, Servicio
from .forms import ClienteRegistrationForm, ClienteUpdateForm, ReservaForm
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


def acerca_de_nosotros(request):
    return render(request, 'paginas/nosotros/acerca_de_nosotros.html')

# Vista para la página de inicio
def inicio(request):
    return render(request, 'paginas/inicio/inicio.html')

# Vista para paquetes
def paquetes(request):
    return render(request, 'paginas/servicios/paquetes.html')

# Vista para ideas
def ideas(request):
    return render(request, 'paginas/servicios/ideas.html')

# Vista de registro de usuarios
def register(request):
    if request.method == 'POST':
        form = ClienteRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")

            # Validar que no exista un User o Cliente con ese email
            if User.objects.filter(email=email).exists():
                form.add_error("email", "Este correo ya está registrado.")
            else:
                user = form.save()
                login(request, user)
                messages.success(request, "Cuenta creada exitosamente.")
                return redirect('inicio')
    else:
        form = ClienteRegistrationForm()

    return render(request, 'registrate.html', {'form': form})

# Vista de login personalizada (opcional, puedes usar LoginView también)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    if not request.user.is_authenticated:
        messages.warning(request, 'Debes iniciar sesión para hacer una reserva.')
    return render(request, 'login.html')

# Vista de logout
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

# Vista del perfil del usuario
@login_required
def perfil_usuario(request):
    try:
        cliente = request.user.cliente
        user = request.user
    except Cliente.DoesNotExist:
        return redirect('registrate')

    if request.method == 'POST':
        form = ClienteUpdateForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
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

def agendar_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)

            nombre = form.cleaned_data.get("nombre")
            apellido = form.cleaned_data.get("apellido")
            email = form.cleaned_data.get("email")
            telefono = form.cleaned_data.get("telefono")
            direccion = form.cleaned_data.get("direccion")
            fecha = form.cleaned_data.get("fecha")
            hora = form.cleaned_data.get("hora")
            servicio = form.cleaned_data.get("servicio")
            paquete = form.cleaned_data.get("paquete")

            if not (nombre and apellido and email and telefono and direccion):
                messages.warning(request, "Debes ingresar todos los datos del formulario.")
            else:
                if hora < time(8, 0) or hora > time(16, 0):
                    messages.warning(request, "La hora seleccionada no es válida. \n El horario permitido es de 08:00am a 04:00pm.")
                else:
                    if request.user.is_authenticated:
                        # Cliente ya existe
                        reserva.cliente = request.user.cliente
                        reserva.save()
                        messages.success(request,
                                         "Reserva creada con éxito. \n Gracias por agendar, te contactaremos para confirmar tu cita.")
                    else:
                        # Crear un nuevo usuario y cliente
                        # 1. Buscar usuario o crearlo con password aleatorio
                        user = User.objects.filter(email=email).first()
                        if user:
                            messages.warning(request, "Cuenta con correo "+email+" ya creado. \n Por favor ingrese a su cuenta para reservar o cambie su correo")
                        else:
                            user = User.objects.create_user(
                                username=email.split("@")[0],
                                email=email,
                                password=get_random_string(10)
                            )

                            # 2. Buscar cliente o crearlo
                            cliente, created = Cliente.objects.get_or_create(
                                user=user,
                                defaults={
                                    "nombre": nombre,
                                    "apellido": apellido,
                                    "email": email,
                                    "telefono": telefono,
                                    "direccion": direccion,
                                }
                            )

                            # 3. Crear reserva
                            reserva = Reserva.objects.create(
                                cliente=cliente,
                                fecha=fecha,
                                hora=hora,
                                servicio=servicio,
                                paquete=paquete
                            )

                            reserva.save()
                            messages.success(request, "Reserva creada con éxito. \n Gracias por agendar, te contactaremos para confirmar tu cita.")
    else:
        form = ReservaForm()

    # Generar calendario del mes actual
    hoy = date.today()
    mes_actual = hoy.month
    año_actual = hoy.year
    cal = calendar.Calendar()
    dias_mes = [d for d in cal.itermonthdates(año_actual, mes_actual) if d.month == mes_actual]
    fecha_default = (timezone.now() + timezone.timedelta(days=1)).date()

    # Contar reservas por día
    dias_ocupados = []
    for d in dias_mes:
        if Reserva.objects.filter(fecha=d).count() >= 3:
            dias_ocupados.append(d.strftime("%Y-%m-%d"))

    return render(request, "reserva_form.html", {
        "form": form,
        "dias_ocupados": mark_safe(json.dumps(dias_ocupados)),  # ✅ lista en JSON
        "mes_actual": mes_actual,
        "año_actual": año_actual,
        "fecha_default": fecha_default
    })

def reserva_exitosa(request):
    return render(request, 'reserva_exitosa.html')


# API para paquetes
def obtener_paquetes(request):
    paquetes = Paquete.objects.all()
    data = [{'id': p.id, 'nombre_paquete': p.nombre_paquete} for p in paquetes]
    return JsonResponse(data, safe=False)



# API para horas
@require_GET
def horas_disponibles(request):
    fecha = request.GET.get('fecha')
    if not fecha:
        return JsonResponse({'error': 'Fecha no proporcionada'}, status=400)

    # Aquí se puede hacer validación real de disponibilidad
    horas_disponibles = [f"{h}:00" for h in range(9, 21)]
    return JsonResponse({'horas_disponibles': horas_disponibles})


# API para pintar eventos en el calendario
def obtener_reservas(request):
    reservas = Reserva.objects.all()
    eventos = []

    for r in reservas:
        eventos.append({
            'title': f"{r.tipo_evento} - {r.cliente.nombre}",
            'start': f"{r.fecha_reserva.date()}T{r.hora.strftime('%H:%M:%S')}",
            'color': '#ffc107',  # amarillo
        })

    return JsonResponse(eventos, safe=False)


# API para guardar la reserva (desde JS)
@csrf_exempt
@login_required
def guardar_reserva_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        paquete_id = data.get('paquete')
        tipo_evento = data.get('tipo_evento')
        hora = data.get('hora')
        fecha = data.get('fecha')

        if not all([paquete_id, tipo_evento, hora, fecha]):
            return JsonResponse({'mensaje': 'Faltan datos'}, status=400)

        if Reserva.objects.filter(fecha=fecha).count() >= 3:
            return JsonResponse({'mensaje': 'Ya hay 3 reservas para esta fecha'}, status=400)

        if Reserva.objects.filter(fecha=fecha, hora=hora).exists():
            return JsonResponse({'mensaje': 'Ya hay una reserva a esa hora'}, status=400)

        paquete = Paquete.objects.get(pk=paquete_id)
        reserva = Reserva.objects.create(
            cliente=request.user.cliente,
            paquete=paquete,
            tipo_evento=tipo_evento,
            hora=hora,
            fecha=fecha
        )

        # Enviar correo
        send_mail(
            'Confirmación de tu reserva',
            f'Reserva confirmada para el {fecha} a las {hora}',
            'tupagina@dominio.com',
            [request.user.email, 'admin@tuweb.com']
        )

        return JsonResponse({'mensaje': 'Reserva guardada correctamente'})

