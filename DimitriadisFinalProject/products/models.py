from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movies_images/', null=True, blank=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title
