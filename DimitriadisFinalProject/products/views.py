from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Movie, Review
from .forms import MovieForm

def products(request):
    movies = Movie.objects.all()
    return render(request, 'products/products.html', {'movies': movies})

def product(request, product_id):
    movie = get_object_or_404(Movie, id=product_id)
    reviews = movie.reviews.all()
    user_review = reviews.filter(user=request.user).first() if request.user.is_authenticated else None

    if request.method == 'POST':
        rating = request.POST.get('rating')  # Rating from the form
        comment = request.POST.get('comment', '')  # Comment from the form

        if not rating:
            messages.error(request, "Please select a star rating.")
        else:
            Review.objects.create(
                movie=movie,
                user=request.user,
                rating=rating,
                comment=comment,
            )
            return redirect('products:product', product_id=product_id)

    context = {
        'movie': movie,
        'reviews': reviews,
        'user_review': user_review,
    }
    return render(request, 'products/product.html', context)

@user_passes_test(lambda u: u.is_superuser)
def addproduct(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:products')
    else:
        form = MovieForm()

    categories = dict(Movie.CATEGORY_CHOICES)
    return render(request, 'products/addproduct.html', {'form': form, 'categories': categories})