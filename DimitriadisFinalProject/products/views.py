from django.shortcuts import render, get_object_or_404
from .models import Movie

def products(request):
    movies = Movie.objects.all()
    return render(request, 'products/products.html', {'movies': movies})

def product_detail(request, product_id):
    movie = get_object_or_404(Movie, id=product_id)
    return render(request, 'products/product_detail.html', {'movie': movie})
