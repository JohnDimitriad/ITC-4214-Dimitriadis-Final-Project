from django.db.models import Avg
from .models import Movie

def get_top_rated_movies(limit=3):
    return (
        Movie.objects.annotate(average_rating=Avg('reviews__rating'))
        .order_by('-average_rating')[:limit]
    )