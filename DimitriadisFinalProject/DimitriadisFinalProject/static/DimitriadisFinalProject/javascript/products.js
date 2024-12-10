document.addEventListener('DOMContentLoaded', function() {
    // Get the category dropdown and all the movie cards
    const categoryFilter = document.getElementById('category_filter');
    const movieCards = document.querySelectorAll('.card');

    // Listen for category filter change
    categoryFilter.addEventListener('change', function() {
        const selectedCategory = categoryFilter.value;

        movieCards.forEach(function(card) {
            const movieCategory = card.getAttribute('data-category'); // Get the category from data-category attribute

            // If selected category is empty, show all movies
            if (selectedCategory === '' || movieCategory === selectedCategory) {
                card.style.display = 'block'; // Show the movie
            } else {
                card.style.display = 'none'; // Hide the movie
            }
        });
    });
});