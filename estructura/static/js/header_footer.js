document.addEventListener('DOMContentLoaded', function() {
    const navItems = document.querySelectorAll('.main-nav > ul > li.has-submenu');
    const headerOverlay = document.querySelector('.header-overlay');

    navItems.forEach(item => {
        const submenu = item.querySelector('.submenu');

        item.addEventListener('mouseenter', function() {
            submenu.style.display = 'block';
            headerOverlay.style.display = 'block';
        });

        item.addEventListener('mouseleave', function() {
            submenu.style.display = 'none';
            headerOverlay.style.display = 'none';
        });
    });
});