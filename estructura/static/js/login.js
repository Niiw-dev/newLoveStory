// Función existente para alternar la visibilidad de la contraseña
function togglePassword() {
    const passwordInput = document.getElementById('password');
    const toggleBtn = document.querySelector('.toggle-password');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleBtn.textContent = '👁️';
    } else {
        passwordInput.type = 'password';
        toggleBtn.textContent = '👁️';
    }
}
// Manejo del envío del formulario
document.getElementById('loginForm').addEventListener('submit', function(e) {
    // Removemos e.preventDefault();
    console.log('Form submitted');
    // El formulario ahora se enviará normalmente al servidor
});

// Nuevo código para el efecto de luz
const toggleSwitch = document.getElementById('toggleSwitch');
const loginContainer = document.querySelector('.login-container');
const lightEffect = document.createElement('div');
lightEffect.classList.add('light-effect');

loginContainer.insertBefore(lightEffect, loginContainer.firstChild);

toggleSwitch.addEventListener('change', function() {
    if (this.checked) {
        loginContainer.classList.add('light-on');
    } else {
        loginContainer.classList.remove('light-on');
    }
});

// Añadir efecto de movimiento al mover el ratón
loginContainer.addEventListener('mousemove', function(e) {
    if (toggleSwitch.checked) {
        const rect = loginContainer.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        lightEffect.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 70%)`;

    }
});