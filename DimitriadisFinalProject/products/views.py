from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import MovieForm, ReviewForm
from .models import Movie, Review

def products(request):
    query = request.GET.get('q', '') 
    category = request.GET.get('category', '') 

    # Filter movies based on search query and category
    movies = Movie.objects.all()
    if query:
        movies = movies.filter(title__icontains=query)
    if category:
        movies = movies.filter(category=category)
    
    context = {'movies': movies}
    return render(request, 'products/products.html', context)

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

def editproduct(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    categories = Movie.CATEGORY_CHOICES

    if request.method == 'POST':
        if 'edit' in request.POST:
            # Edit movie
            form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('products:products')
        elif 'delete' in request.POST:
            # Delete movie
            movie.delete()
            return redirect('products:products')

    else:
        form = MovieForm(instance=movie)

    return render(request, 'products/editproduct.html', {'form': form, 'movie': movie, 'categories': categories})