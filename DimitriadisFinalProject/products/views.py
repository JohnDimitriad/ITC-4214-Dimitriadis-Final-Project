from django.shortcuts import render, get_object_or_404
from .models import Movie

def product_list(request):
    movies = Movie.objects.all()
    return render(request, 'products/product_list.html', {'movies': movies})

def product_detail(request, product_id):
    movie = get_object_or_404(Movie, id=product_id)
    return render(request, 'products/product_detail.html', {'movie': movie})
