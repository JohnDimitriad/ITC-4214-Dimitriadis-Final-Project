from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('sci-fi', 'Science Fiction'),
        ('comedy', 'Comedy'),
        ('thriller', 'Thriller'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='action')

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return sum(review.rating for review in reviews) / reviews.count()
        return 0

    def __str__(self):
        return self.title
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} - {self.rating} Stars'