document.getElementById('delete-btn').addEventListener('click', function() {
    if (confirm('Are you sure you want to delete this movie?')) {
        const form = document.getElementById('delete-form');
        
        // Send the POST request via AJAX
        fetch(form.action, {
            method: 'POST',
            body: new FormData(form),
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Remove the movie from the page or reload the page
                alert('Movie deleted successfully!');
                window.location.href = '{% url "products:products" %}';  // Redirect to the products list page
            } else {
                alert('Failed to delete movie!');
            }
        })
        .catch(error => {
            alert('Error deleting movie.');
            console.error(error);
        });
    }
});