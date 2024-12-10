from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import MovieForm, ReviewForm
from django.http import JsonResponse
from django.contrib import messages
from .models import Movie, Review

def products(request):
    movies = Movie.objects.all()
    return render(request, 'products/products.html', {'movies': movies})

def product(request, product_id):
    movie = get_object_or_404(Movie, id=product_id)
    reviews = Review.objects.filter(movie=movie)
    user_review = None

    if request.user.is_authenticated:
        # Check if the user has already reviewed this movie
        user_review = reviews.filter(user=request.user).first()

        # Handle review submission
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.user = request.user
                review.save()
                # Redirect to the same page to refresh and show the new review
                return redirect('products:product', product_id=movie.id)
        else:
            form = ReviewForm()
    else:
        form = None

    context = {
        'movie': movie,
        'reviews': reviews,
        'user_review': user_review,
        'form': form,
    }

    return render(request, 'products/product.html', context)

@user_passes_test(lambda u: u.is_superuser)
def addproduct(request):
    categories = Movie.CATEGORY_CHOICES
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:products')
    else:
        form = MovieForm()
    
    return render(request, 'products/addproduct.html', {'form': form, 'categories': categories})