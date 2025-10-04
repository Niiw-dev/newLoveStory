document.addEventListener('DOMContentLoaded', function() {
    // Datos de ejemplo (reemplaza esto con tus datos reales o una llamada a la API)
    const paquetes = [
        {
            id: 1,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto9.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 2,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto8.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 3,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto7.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 4,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto6.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 5,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto5.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 6,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto4.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 7,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto3.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 8,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto2.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 9,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto1.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 10,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto9.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 11,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto8.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 12,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto1.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 13,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto5.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 14,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto7.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 15,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto3.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 16,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto8.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 17,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto5.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 18,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto7.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 19,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto2.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 20,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto6.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 21,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto8.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 22,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto1.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        {
            id: 23,
            nombre: "Paquete Básico",
            descripcion: "Perfecto para eventos pequeños",
            precio: "$500",
            imagen: '/static/images/Foto9.jpeg',
            contenido: ["2 horas de cobertura", "100 fotos editadas", "Galería digital"]
        },
        {
            id: 24,
            nombre: "Paquete Estándar",
            descripcion: "Ideal para bodas y eventos medianos",
            precio: "$1000",
            imagen: '/static/images/Foto6.jpeg',
            contenido: ["4 horas de cobertura", "200 fotos editadas", "Álbum impreso", "Galería digital"]
        },
        // ... Agrega más paquetes aquí hasta tener al menos 20 para la paginación
    ];

    
    const paquetesGrid = document.getElementById('paquetes-grid');
    const prevPageBtn = document.getElementById('prev-page');
    const nextPageBtn = document.getElementById('next-page');
    const currentPageSpan = document.getElementById('current-page');
    const totalPagesSpan = document.getElementById('total-pages');
    const modal = document.getElementById('paquete-modal');
    const modalTitle = document.getElementById('modal-title');
    const modalDescription = document.getElementById('modal-description');
    const modalPrice = document.getElementById('modal-price');
    const modalContenido = document.getElementById('modal-contenido');
    const modalReserva = document.getElementById('modal-reserva');
    const modalInfo = document.getElementById('modal-info');
    const closeModal = document.querySelector('.close');

    let currentPage = 1;
    const paquetesPorPagina = 10;
    const totalPages = Math.ceil(paquetes.length / paquetesPorPagina);

    // Función para mostrar los paquetes por página
    function mostrarPaquetes(page) {
        const inicio = (page - 1) * paquetesPorPagina;
        const fin = inicio + paquetesPorPagina;
        const paquetesPagina = paquetes.slice(inicio, fin);

        // Limpiar el grid de paquetes
        paquetesGrid.innerHTML = '';

        // Insertar cada paquete en la página actual
        paquetesPagina.forEach(paquete => {
            const paqueteCard = document.createElement('div');
            paqueteCard.className = 'paquete-card';
            paqueteCard.innerHTML = `
                <img src="${paquete.imagen}" alt="${paquete.nombre}">
                <div class="paquete-info">
                    <h3>${paquete.nombre}</h3>
                    <p>${paquete.descripcion}</p>
                    <p>${paquete.precio}</p>
                </div>
            `;
            paqueteCard.addEventListener('click', () => mostrarModal(paquete));
            paquetesGrid.appendChild(paqueteCard);
        });

        // Actualizar el estado de la paginación
        currentPageSpan.textContent = page;
        totalPagesSpan.textContent = totalPages;
        prevPageBtn.disabled = page === 1;
        nextPageBtn.disabled = page === totalPages;
    }

    // Función para mostrar el modal con los detalles del paquete
    function mostrarModal(paquete) {
        modalTitle.textContent = paquete.nombre;
        modalDescription.textContent = paquete.descripcion;
        modalPrice.textContent = `Precio: ${paquete.precio}`;
        modalContenido.innerHTML = paquete.contenido.map(item => `<li>${item}</li>`).join('');
        modalReserva.href = `/reservas/?paquete_id=${paquete.id}`;
        modalInfo.href = `/info/${paquete.id}`;
        modal.style.display = 'block';
    }

    // Paginación: navegar a la página anterior
    prevPageBtn.addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            mostrarPaquetes(currentPage);
        }
    });

    // Paginación: navegar a la página siguiente
    nextPageBtn.addEventListener('click', () => {
        if (currentPage < totalPages) {
            currentPage++;
            mostrarPaquetes(currentPage);
        }
    });

    // Cerrar el modal
    closeModal.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    // Cerrar el modal si se hace clic fuera de él
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Mostrar los paquetes de la primera página al cargar
    mostrarPaquetes(currentPage);
});