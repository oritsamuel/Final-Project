from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta: 
        model = Movie
        fields = ('title', 'director', 'description', 'genre', 'created_at', 'rating', 'image')

