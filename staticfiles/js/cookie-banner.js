document.addEventListener('DOMContentLoaded', function() {
    const cookieBanner = document.getElementById('cookie-banner');
    const cookieAccept = document.getElementById('cookie-accept');
    const cookieSettings = document.getElementById('cookie-settings');
    const cookieSettingsModal = document.getElementById('cookie-settings-modal');
    const cookieClose = document.querySelector('.cookie-close');
    const savePreferences = document.getElementById('save-preferences');
    
    // Para pruebas: eliminar esto después de verificar que funciona
    localStorage.removeItem('cookiesAccepted');

    // Comprobar si el usuario ya ha aceptado las cookies
    const cookiesAccepted = localStorage.getItem('cookiesAccepted');

    if (!cookiesAccepted) {
        // Mostrar el banner inmediatamente al cargar la página
        setTimeout(() => {
            cookieBanner.style.display = 'flex'; // Cambiado a flex para centrar
        }, 500); // Pequeño retraso para asegurar que todo esté cargado
    }

    // Función para aceptar todas las cookies
    function acceptAllCookies() {
        localStorage.setItem('cookiesAccepted', 'true');
        localStorage.setItem('analyticsCookies', 'true');
        localStorage.setItem('marketingCookies', 'true');

        // Añadir animación de desvanecimiento
        cookieBanner.style.opacity = '0';
        setTimeout(() => {
            cookieBanner.style.display = 'none';
            cookieBanner.style.opacity = '1';
        }, 500);

        cookieSettingsModal.style.display = 'none';
    }

    // Función para guardar preferencias de cookies
    function savePreferencesHandler() {
        localStorage.setItem('cookiesAccepted', 'true');
        localStorage.setItem('analyticsCookies', document.getElementById('analytics-cookies').checked ? 'true' : 'false');
        localStorage.setItem('marketingCookies', document.getElementById('marketing-cookies').checked ? 'true' : 'false');

        // Añadir animación de desvanecimiento
        cookieBanner.style.opacity = '0';
        setTimeout(() => {
            cookieBanner.style.display = 'none';
            cookieBanner.style.opacity = '1';
        }, 500);

        cookieSettingsModal.style.display = 'none';
    }

    // Event listeners
    cookieAccept.addEventListener('click', acceptAllCookies);

    cookieSettings.addEventListener('click', function() {
        cookieSettingsModal.style.display = 'flex'; // Cambiado a flex para centrar
    });

    cookieClose.addEventListener('click', function() {
        cookieSettingsModal.style.display = 'none';
    });

    savePreferences.addEventListener('click', savePreferencesHandler);

    // Cerrar el modal al hacer clic fuera de él
    window.addEventListener('click', function(event) {
        if (event.target === cookieSettingsModal) {
            cookieSettingsModal.style.display = 'none';
        }
    });

    // Cargar preferencias guardadas en el modal
    if (localStorage.getItem('analyticsCookies') === 'false') {
        document.getElementById('analytics-cookies').checked = false;
    }

    if (localStorage.getItem('marketingCookies') === 'false') {
        document.getElementById('marketing-cookies').checked = false;
    }

    // Para pruebas: botón para mostrar el banner manualmente
    console.log('Script de cookies cargado');
});