document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        if (this.hash !== "") {
            e.preventDefault();
            const hash = this.hash;
            const targetElement = document.querySelector(hash);

            if (targetElement) {
                const headerHeight = 56;
                const navHeight = 50;
                const offset = targetElement.offsetTop - (headerHeight + navHeight + 20);
                window.scrollTo({
                    top: offset,
                    behavior: 'smooth'
                });
            }
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const carouselElement = document.getElementById('carouselPromocoes');
    if (carouselElement) {
        new bootstrap.Carousel(carouselElement, {
            interval: 5000
        });
    }
});