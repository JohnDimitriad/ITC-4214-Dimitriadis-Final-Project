$(document).ready(function() {
    $('#review-form').submit(function(event) {
        event.preventDefault();

        var form = $(this);
        var formData = form.serialize();

        $.ajax({
            url: form.attr('action'),
            type: 'POST',
            data: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            success: function(response) {
                window.location.reload();
            },
            error: function() {
                alert('Error submitting review');
            }
        });
    });
});
