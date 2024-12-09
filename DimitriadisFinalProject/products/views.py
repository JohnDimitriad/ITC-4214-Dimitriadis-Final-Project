from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

def products(request):
    movies = Movie.objects.all()
    return render(request, 'products/products.html', {'movies': movies})

def product(request, product_id):
    movie = get_object_or_404(Movie, pk=product_id)
    return render(request, 'products/product.html', {'movie': movie})


#superuser adding movies
@user_passes_test(lambda u: u.is_superuser)
def addproduct(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie added successfully!')
            return redirect('products:products')
    else:
        form = MovieForm()
    return render(request, 'products/addproduct.html', {'form': form})