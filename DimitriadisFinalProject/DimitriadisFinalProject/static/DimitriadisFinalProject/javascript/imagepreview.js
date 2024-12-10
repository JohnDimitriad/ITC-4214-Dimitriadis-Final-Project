function previewImage(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function() {
        const imagePreview = document.querySelector('#imagePreview');
        
        if (imagePreview) {
            imagePreview.src = reader.result;
            imagePreview.style.display = 'block';
        }
    };

    if (file) {
        reader.readAsDataURL(file);
    }
}