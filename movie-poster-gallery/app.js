// Insert images dynamically into the carousel
window.onload = function() {
    const carousel = document.querySelector('.carousel');
  
    // Add images to the carousel (adjust the path to your image folder)
    const imageFolder = 'S:\\Fun-projects\\movie-poster-gallery\\uploaded_posters'; // Replace with the correct folder path
    const images = ['albert_einstein.jpg', 'apj_abdul_kalam.jpg', 'charles_darwin.jpg', 'elon_musk.jpg', 'geoffrey_hinton.jpg', 'isaac_newton.jpg', 'nicola_tesla.jpg', 'madame_curie.jpg']; // Add your image filenames
  
    images.forEach(image => {
      const imgElement = document.createElement('img');
      imgElement.src = `${imageFolder}/${image}`; // Adjust path as necessary
      imgElement.alt = 'Movie Poster';
      carousel.appendChild(imgElement);
    });
  
    // Stop the scrolling when hovering over the images
    const carouselImages = document.querySelectorAll('.carousel img');
    carouselImages.forEach(image => {
      image.addEventListener('mouseenter', () => {
        document.querySelector('.carousel').style.animationPlayState = 'paused';
      });
      image.addEventListener('mouseleave', () => {
        document.querySelector('.carousel').style.animationPlayState = 'running';
      });
    });
  };
  