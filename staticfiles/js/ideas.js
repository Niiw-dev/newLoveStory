document.addEventListener('DOMContentLoaded', function() {
    // Datos de ejemplo (reemplaza esto con tus datos reales o una llamada a la API)
    const eventos = [
        {
            id: 1,
            titulo: 'Boda en la Playa',
            descripcion: 'Una hermosa boda al atardecer en la playa de Cartagena.',
            fecha: '2023-11-15',
            ubicacion: 'Playa Blanca, Cartagena',
            imagenes: [
                '/static/images/Foto9.jpeg',
                '/static/images/Foto5.jpeg',
                '/static/images/Foto7.jpeg',
            ],
        },
        {
            id: 2,
            titulo: 'Sesión Pre-Boda en el Parque',
            descripcion: 'Capturando momentos especiales antes del gran día.',
            fecha: '2023-10-20',
            ubicacion: 'Parque Simón Bolívar, Bogotá',
            imagenes: [
                '/static/images/Foto2.jpeg',
                '/static/images/Foto3.jpeg',
                '/static/images/Foto6.jpeg',
            ],
        },
        // Agrega más eventos aquí
    ];

    let currentEventIndex = 0;
    let currentImageIndex = 0;

    const carouselContainer = document.querySelector('.carousel-container');
    const prevButton = document.querySelector('.carousel-button.prev');
    const nextButton = document.querySelector('.carousel-button.next');
    const eventTitle = document.getElementById('event-title');
    const eventDescription = document.getElementById('event-description');
    const eventDate = document.getElementById('event-date');
    const eventLocation = document.getElementById('event-location');
    const eventGrid = document.querySelector('.event-grid');

    function updateEventDisplay() {
        const event = eventos[currentEventIndex];
        eventTitle.textContent = event.titulo;
        eventDescription.textContent = event.descripcion;
        eventDate.textContent = event.fecha;
        eventLocation.textContent = event.ubicacion;

        carouselContainer.innerHTML = '';
        event.imagenes.forEach(src => {
            const img = document.createElement('img');
            img.src = src;
            img.alt = event.titulo;
            carouselContainer.appendChild(img);
        });
        updateCarousel();
    }

    function updateCarousel() {
        const width = carouselContainer.clientWidth;
        carouselContainer.style.transform = `translateX(-${currentImageIndex * width}px)`;
    }

    prevButton.addEventListener('click', () => {
        if (currentImageIndex > 0) {
            currentImageIndex--;
            updateCarousel();
        }
    });

    nextButton.addEventListener('click', () => {
        if (currentImageIndex < eventos[currentEventIndex].imagenes.length - 1) {
            currentImageIndex++;
            updateCarousel();
        }
    });

    function createEventCards() {
        eventos.forEach((event, index) => {
            const card = document.createElement('div');
            card.className = 'event-card';
            card.innerHTML = `
                <img src="${event.imagenes[0]}" alt="${event.titulo}">
                <div class="event-card-content">
                    <h3>${event.titulo}</h3>
                    <button>Seleccionar</button>
                </div>
            `;
            card.querySelector('button').addEventListener('click', () => {
                currentEventIndex = index;
                currentImageIndex = 0;
                updateEventDisplay();
            });
            eventGrid.appendChild(card);
        });
    }

    updateEventDisplay();
    createEventCards();

    window.addEventListener('resize', updateCarousel);
});