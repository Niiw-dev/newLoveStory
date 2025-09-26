document.addEventListener("DOMContentLoaded", function () {
    const servicioSelect = document.getElementById("servicio");
    const tipoEventoSelect = document.getElementById("tipo-evento");
    const horaSelect = document.getElementById("hora");
    const botonReserva = document.getElementById("boton-reserva");

    // Cargar paquetes desde el backend
    fetch("/api/paquetes/")
        .then((response) => response.json())
        .then((data) => {
            data.forEach((item) => {
                const option = document.createElement("option");
                option.value = item.id;
                option.textContent = item.nombre_paquete;
                servicioSelect.appendChild(option);
            });
        });

    // Cuando se selecciona un paquete, habilita tipo de evento
    servicioSelect.addEventListener("change", () => {
        if (servicioSelect.value !== "") {
            tipoEventoSelect.disabled = false;
        } else {
            tipoEventoSelect.disabled = true;
            tipoEventoSelect.value = "";
            horaSelect.disabled = true;
            horaSelect.innerHTML = `<option value="">Selecciona una hora</option>`;
        }
    });

    // Cuando se selecciona tipo de evento, habilita selector de hora
    tipoEventoSelect.addEventListener("change", () => {
        if (tipoEventoSelect.value !== "") {
            const fechaSeleccionada = document.getElementById("fecha-seleccionada").textContent;
            fetch(`/api/horas-disponibles/?fecha=${fechaSeleccionada}`)
                .then((response) => response.json())
                .then((data) => {
                    horaSelect.innerHTML = `<option value="">Selecciona una hora</option>`;
                    data.horas_disponibles.forEach((hora) => {
                        const option = document.createElement("option");
                        option.value = hora;
                        option.textContent = hora;
                        horaSelect.appendChild(option);
                    });
                    horaSelect.disabled = false;
                });
        } else {
            horaSelect.disabled = true;
        }
    });

    // Habilitar botón de reserva si todo está seleccionado
    horaSelect.addEventListener("change", () => {
        if (horaSelect.value !== "") {
            botonReserva.disabled = false;
        } else {
            botonReserva.disabled = true;
        }
    });
});