document.getElementById('accessibility-button').addEventListener('click', function() {
    var menu = document.getElementById('accessibility-menu');
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
});

function toggleDarkMode() {
    var body = document.body;
    body.classList.toggle('dark-mode');
    var iconElement = document.getElementById('dark-mode-icon');
    
    if (body.classList.contains('dark-mode')) {
        iconElement.src = "{% static 'images/Luna.png' %}"; // Icono de luna
    } else {
        iconElement.src = "{% static 'images/Sol.png' %}"; // Icono de sol
    }
}

function increaseFontSize() {
    document.body.style.fontSize = 'larger';
}

function decreaseFontSize() {
    document.body.style.fontSize = 'smaller';
}

function translateContent() {
    const elementsToTranslate = document.querySelectorAll('[data-translate]');
    
    elementsToTranslate.forEach(element => {
        const translation = translations[element.getAttribute('data-translate')];
        if (translation) {
            element.textContent = translation;
        }
    });
}

// Función para mantener el menú cerrado al hacer clic fuera de él
window.onclick = function(event) {
    var menu = document.getElementById('accessibility-menu');
    if (!event.target.matches('#accessibility-button') && !menu.contains(event.target)) {
        menu.style.display = 'none';
    }
};

// Traducciones para el botón de traducir
const translations = {
    'Modo Oscuro/Claro': 'Dark Mode/Light Mode',
    'Aumentar Tamaño de Letra': 'Increase Font Size',
    'Disminuir Tamaño de Letra': 'Decrease Font Size',
    'Traducir': 'Translate'
    // Añadir más traducciones aquí
};

// Agregar iconos a los botones
document.getElementById('toggle-dark-mode').insertAdjacentHTML('afterbegin', '<img id="dark-mode-icon" class="icon" src="{% static \'icons/sun-icon.svg\' %}" alt="Dark Mode Icon"> ');
document.getElementById('increase-font-size').insertAdjacentHTML('afterbegin', '<img class="icon" src="{% static \'icons/arrow-up-icon.svg\' %}" alt="Increase Font Size Icon"> ');
document.getElementById('decrease-font-size').insertAdjacentHTML('afterbegin', '<img class="icon" src="{% static \'icons/arrow-down-icon.svg\' %}" alt="Decrease Font Size Icon"> ');
document.getElementById('translate-button').insertAdjacentHTML('afterbegin', '<img class="icon" src="{% static \'icons/dictionary-icon.svg\' %}" alt="Translate Icon"> ');

document.querySelector('.btn-ayuda').addEventListener('click', function() {
    // Aquí puedes abrir un modal o redirigir a una página de preguntas frecuentes
    alert('Aquí iría el contenido de ayuda y preguntas frecuentes.');
});

document.addEventListener('click', function(event) {
    var userMenuContainer = document.querySelector('.user-menu-container');
    var userMenu = document.querySelector('.user-menu');
    
    if (!userMenuContainer.contains(event.target)) {
        userMenu.style.display = 'none';
    } else {
        userMenu.style.display = 'block';
    }
});
