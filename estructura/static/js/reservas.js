document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendario');
    var formularioReserva = document.getElementById('formulario-reserva');
    var fechaSeleccionadaEl = document.getElementById('fecha-seleccionada');
    var selectorHora = document.getElementById('hora');
    var selectorServicio = document.getElementById('servicio');
    var selectorTipoEvento = document.getElementById('tipo-evento'); // Selector para el tipo de evento (8 o 11 horas)
    var botonReserva = document.getElementById('boton-reserva');
    var fechaSeleccionada;

    // Referencia al elemento img que queremos cambiar
    var imagenMes = document.getElementById('imagen-mes');

    // Mapeo de meses a imágenes
    const imagenesPorMes = {
        0: '/static/images/Calendario 1.jpeg',
        1: '/static/images/Calendario 2.jpeg',
        2: '/static/images/Calendario 3.jpeg',
        3: '/static/images/Calendario 4.jpeg',
        4: '/static/images/Calendario 5.jpeg',
        5: '/static/images/Calendario 6.jpeg',
        6: '/static/images/Calendario 7.jpeg',
        7: '/static/images/Calendario 8.jpeg',
        8: '/static/images/Calendario 9.jpeg',
        9: '/static/images/Calendario 10.jpeg',
        10: '/static/images/Calendario 11.jpeg',
        11: '/static/images/Calendario 12.jpeg',
    };

    // Función para cambiar la imagen según el mes
    function cambiarImagenPorMes(fechaActual) {
        var mes = fechaActual.getMonth(); // Obtenemos el mes actual
        var nuevaImagen = imagenesPorMes[mes] || "{% static 'images/default.jpg' %}"; // Fallback en caso de que no haya imagen para ese mes
        imagenMes.src = nuevaImagen; // Cambiamos la imagen
    }

    // Función para generar las horas según el tipo de evento
    function generarHoras(tipoEvento) {
        selectorHora.innerHTML = '<option value="">Selecciona una hora</option>';  // Limpiar las opciones anteriores
        let horasDisponibles = [];

        if (tipoEvento === '8') {
            // Horas para eventos de 8 horas
            horasDisponibles = ['09:00', '10:00', '11:00', '12:00'];
        } else if (tipoEvento === '11') {
            // Horas para eventos de 11 horas
            horasDisponibles = ['08:00', '09:00', '10:00', '11:00'];
        }

        horasDisponibles.forEach(function(hora) {
            var option = document.createElement('option');
            option.value = hora;
            option.text = hora;
            selectorHora.appendChild(option);
        });

        // Habilitar el selector de horas
        selectorHora.disabled = false;
    }

    // Evento cuando el cliente selecciona un servicio o paquete
    selectorServicio.addEventListener('change', function() {
        if (selectorServicio.value !== '') {
            // Habilitar la selección del tipo de evento
            selectorTipoEvento.disabled = false;
        } else {
            selectorTipoEvento.disabled = true;
            selectorHora.disabled = true;
            botonReserva.disabled = true;
        }
    });

    // Evento cuando el cliente selecciona el tipo de evento (8 o 11 horas)
    selectorTipoEvento.addEventListener('change', function() {
        if (selectorTipoEvento.value !== '') {
            // Generar horas basadas en el tipo de evento
            generarHoras(selectorTipoEvento.value);
        } else {
            selectorHora.disabled = true;
        }
    });

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        selectable: true,
        selectMirror: true,
        dayMaxEvents: true,
        locale: 'es',
        events: '/api/obtener-reservas/',
        select: function(info) {
            fechaSeleccionada = info.startStr;
            fechaSeleccionadaEl.textContent = fechaSeleccionada;
            formularioReserva.style.display = 'block';
            calendar.unselect();
        },
        eventClick: function(info) {
            alert('Detalles de la reserva:\n' + 
                  'Servicio: ' + info.event.title + '\n' +
                  'Fecha: ' + info.event.start.toLocaleString() + '\n' +
                  'Estado: ' + (info.event.extendedProps.estado ? 'Activa' : 'Cancelada'));
        },
        eventClassNames: function(arg) {
            if (!arg.event.extendedProps.estado) {
                return ['evento-cancelado'];
            }
            return [];
        },
        // Evento que se dispara cuando cambia la vista (incluye el cambio de mes)
        datesSet: function(info) {
            // Llamamos a la función para cambiar la imagen por mes
            cambiarImagenPorMes(info.start);
        }
    });

    calendar.render();

    botonReserva.addEventListener('click', function() {
        const horaSeleccionada = selectorHora.value;
        const servicioSeleccionado = selectorServicio.value;

        if (!fechaSeleccionada || !horaSeleccionada || !servicioSeleccionado) {
            alert('Por favor, selecciona una fecha, hora y servicio');
            return;
        }

        fetch('/api/hacer-reserva/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                fecha: fechaSeleccionada,
                hora: horaSeleccionada,
                servicio: servicioSeleccionado
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                alert(data.mensaje);
                calendar.refetchEvents();
                formularioReserva.style.display = 'none';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Hubo un error al hacer la reserva');
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Cambiar la imagen al cargar por primera vez
    cambiarImagenPorMes(new Date());
});
