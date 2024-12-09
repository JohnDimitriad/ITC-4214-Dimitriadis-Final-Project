from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'category', 'image']
        widgets = {
            'category': forms.Select(choices=Movie.CATEGORY_CHOICES),
        }