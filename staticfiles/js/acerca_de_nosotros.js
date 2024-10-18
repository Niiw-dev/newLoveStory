document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.carousel-items');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    
    prevButton.addEventListener('click', () => {
        carousel.scrollBy({ left: -carousel.offsetWidth, behavior: 'smooth' });
    });
    
    nextButton.addEventListener('click', () => {
        carousel.scrollBy({ left: carousel.offsetWidth, behavior: 'smooth' });
    });
});