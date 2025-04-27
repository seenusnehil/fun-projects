document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.querySelector('.carousel');
    
    // List of image URLs
    const imagePaths = [
        'uploaded_posters/albert_einstein.png',
        'uploaded_posters/elon_musk.png',
        'uploaded_posters/madame_curie.png',
        'uploaded_posters/charles_darwin.png',
        'uploaded_posters/nicola_tesla.png',
        'uploaded_posters/apj_abdul_kalam.png',
        'uploaded_posters/geoffrey_hinton.png',
        'uploaded_posters/isaac_newton.png'
    ];

    // Loop through each image path and create an img element for each
    imagePaths.forEach(path => {
        const img = document.createElement('img');
        img.src = path;
        img.alt = 'Movie Poster';
        img.classList.add('poster');
        carousel.appendChild(img);
    });

    // Duplicate the images to create a continuous loop effect
    const clonedImages = carousel.innerHTML;
    carousel.innerHTML += clonedImages;
});
