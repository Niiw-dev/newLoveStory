import os
from datetime import datetime, date, time, timedelta
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_calendar_service():
    creds = None
    token_path = os.path.join(os.getcwd(), 'token.json')  # aquí se guarda el token
    credentials_path = os.path.join(os.getcwd(), 'estructura', 'credentials.json')

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=8080)

        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)


def crear_evento_google_calendar(reserva):
    service = get_calendar_service()

    fecha_hora_inicio = datetime(
        reserva.fecha.year,
        reserva.fecha.month,
        reserva.fecha.day,
        reserva.hora.hour,
        reserva.hora.minute
    )
    fecha_hora_fin = fecha_hora_inicio + timedelta(hours=1)

    event = {
        'summary': f"Reserva pendiente - {reserva.servicio.tipo_de_servicio}",
        'description': (
            f"Cliente: {reserva.cliente.nombre} {reserva.cliente.apellido}\n"
            f"Email: {reserva.cliente.email}\n"
            f"Tel: {reserva.cliente.telefono}\n\n"
            f"Paquete: {reserva.paquete.nombre_paquete}\n"
            f"Monto: ${reserva.monto}\n"
            f"Límite de pago: {reserva.limite_pago.strftime('%d/%m/%Y %H:%M')}\n"
            f"Referencia: {reserva.payment_reference}"
        ),
        'start': {'dateTime': fecha_hora_inicio.isoformat(), 'timeZone': 'America/Bogota'},
        'end': {'dateTime': fecha_hora_fin.isoformat(), 'timeZone': 'America/Bogota'},
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 60},  # recordatorio 1h antes
                {'method': 'popup', 'minutes': 10},  # recordatorio 10 min antes
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"✅ Evento creado en Google Calendar: {event.get('htmlLink')}")
