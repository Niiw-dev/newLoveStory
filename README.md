# 💖 Love Story — Plataforma de Agendamiento Fotográfico

> 💬 *Proyecto de grado SENA desarrollado en equipo. Implementé el módulo de agendamiento de citas, enfocado en optimizar la gestión de reservas para eventos especiales.*

---

### 📸 Descripción
**Love Story** es una plataforma web desarrollada con **Python y Django**, diseñada para que una **agencia fotográfica** gestione sus citas y reservas de manera automatizada.  
Permite a los clientes **agendar sesiones fotográficas**, confirmar horarios disponibles y recibir **notificaciones automáticas por correo electrónico y Google Calendar**.

El sistema fue construido con un enfoque en la **experiencia del cliente y la eficiencia administrativa**, integrando herramientas modernas que mejoran la organización interna del estudio.

---

### 💎 Características Principales
- 📅 **Agendamiento de citas fotográficas** con selección de fecha y hora.  
- 📧 **Notificaciones automáticas** por correo al confirmar la cita.  
- 🗓️ **Integración con Google Calendar** para registrar eventos.  
- 👥 **Panel administrativo** para la gestión de servicios y reservas.  
- 🧭 **Diseño intuitivo y adaptable** pensado para clientes y administradores.  

---

### 🛠️ Tecnologías Utilizadas
- **Backend:** Python, Django  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Base de datos:** MySQL  
- **Integraciones:** API de Google Calendar, servicio de correo electrónico  

---

### ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Niiw-dev/newLoveStory.git
   ```

---

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```
4. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

---

### 🚀 Uso
El sistema permite:
- Reservar citas para sesiones fotográficas y eventos especiales.  
- Confirmar horarios disponibles y recibir notificaciones por correo.  
- Registrar automáticamente las citas en Google Calendar.  
- Administrar servicios, usuarios y reservas desde el panel interno.  

---

### 🧩 Estructura del Proyecto
```textplain
📦 cuerpoSano
 ┣ 📂 estructura/          # Lógica principal del sistema de agendamiento y reservas
 ┣ 📂 sistema/             # Configuración base del proyecto Django (ajustes, URLs, apps)
 ┣ 📂 staticfiles/         # Archivos estáticos (CSS, JS, imágenes)
 ┣ 📜 DockerDB.yml         # Configuración de base de datos y servicios con Docker
 ┣ 📜 manage.py            # Script principal para ejecutar tareas de Django
 ┣ 📜 requirements.txt     # Dependencias del proyecto
 ┗ 📜 README.md            # Documentación general del proyecto
```

---

### 👨‍💻 Autor
Creado con 💙 por **[Niiw.Dev](https://github.com/Niiw-dev)**  
   
