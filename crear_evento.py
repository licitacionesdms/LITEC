from google.oauth2 import service_account
from googleapiclient.discovery import build

# Definir la ruta del archivo de credenciales
SERVICE_ACCOUNT_FILE = r"C:\Users\danna\djangotutorial\credentials.json"

# Definir el alcance (permisos)
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Autenticación con la cuenta de servicio
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Construir el servicio de Google Calendar
service = build("calendar", "v3", credentials=creds)

# Definir el evento
event = {
    "summary": "Google I/O 2025",
    "location": "800 Howard St., San Francisco, CA 94103",
    "description": "A chance to hear more about Google's developer products.",
    "start": {
        "dateTime": "2025-05-28T09:00:00-07:00",
        "timeZone": "America/Los_Angeles",
    },
    "end": {
        "dateTime": "2025-05-28T17:00:00-07:00",
        "timeZone": "America/Los_Angeles",
    },
    "recurrence": ["RRULE:FREQ=DAILY;COUNT=2"],
    "attendees": [
        {"email": "lpage@example.com"},
        {"email": "sbrin@example.com"},
    ],
    "reminders": {
        "useDefault": False,
        "overrides": [
            {"method": "email", "minutes": 24 * 60},
            {"method": "popup", "minutes": 10},
        ],
    },
}

# Insertar el evento en el calendario
event = service.events().insert(calendarId="primary", body=event).execute()

# Imprimir el enlace del evento creado
print("Evento creado: {}".format(event.get("htmlLink")))