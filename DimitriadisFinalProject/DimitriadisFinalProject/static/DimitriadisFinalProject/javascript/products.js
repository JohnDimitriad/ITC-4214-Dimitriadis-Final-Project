document.addEventListener("DOMContentLoaded", function () {
    // Elements
    const searchInput = document.getElementById("search_bar");
    const searchButton = document.getElementById("search_button");
    const categorySelect = document.getElementById("category_filter");
    const movieItems = document.querySelectorAll(".movie-item");

    // Search bar functionality
    function searchMovies() {
        const searchTerm = searchInput.value.toLowerCase();

        movieItems.forEach(function (movie) {
            const movieTitle = movie.querySelector(".card-title").textContent.toLowerCase();
            const movieDescription = movie.querySelector(".card-text").textContent.toLowerCase();

            if (movieTitle.includes(searchTerm) || movieDescription.includes(searchTerm)) {
                movie.style.display = "block";  // Show movie
            } else {
                movie.style.display = "none";   // Hide movie
            }
        });
    }

    // Event listener for search button
    searchButton.addEventListener("click", searchMovies);

    categorySelect.addEventListener("change", function () {
        const selectedCategory = categorySelect.value.toLowerCase();
        
        movieItems.forEach(function (movie) {
            const categoryText = movie.querySelector(".text-muted").textContent.toLowerCase();
            
            if (selectedCategory === "" || categoryText.includes(selectedCategory)) {
                movie.style.display = "block";  // Show movie
            } else {
                movie.style.display = "none";   // Hide movie
            }
        });
    });
});
