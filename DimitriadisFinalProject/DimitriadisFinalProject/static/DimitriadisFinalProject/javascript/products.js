document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector("#search_bar");
    const searchButton = document.querySelector("#search_button");
    const categorySelect = document.querySelector("#category_filter");
    const movieItems = document.querySelectorAll(".movie-item");

    // Function to filter movies based on the search term
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

    // Function to filter movies based on the selected category
    function filterByCategory() {
        const selectedCategory = categorySelect.value.toLowerCase();

        movieItems.forEach(function (movie) {
            const categoryText = movie.querySelector(".text-muted").textContent.toLowerCase();

            if (selectedCategory === "" || categoryText.includes(selectedCategory)) {
                movie.style.display = "block";  // Show movie
            } else {
                movie.style.display = "none";   // Hide movie
            }
        });
    }

    // Combine search and category filters
    function applyFilters() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedCategory = categorySelect.value.toLowerCase();

        movieItems.forEach(function (movie) {
            const movieTitle = movie.querySelector(".card-title").textContent.toLowerCase();
            const movieDescription = movie.querySelector(".card-text").textContent.toLowerCase();
            const categoryText = movie.querySelector(".text-muted").textContent.toLowerCase();

            const matchesSearch =
                movieTitle.includes(searchTerm) || movieDescription.includes(searchTerm);
            const matchesCategory =
                selectedCategory === "" || categoryText.includes(selectedCategory);

            if (matchesSearch && matchesCategory) {
                movie.style.display = "block";  // Show movie
            } else {
                movie.style.display = "none";   // Hide movie
            }
        });
    }

    // Event listeners
    searchButton.addEventListener("click", applyFilters);
    categorySelect.addEventListener("change", applyFilters);
});
