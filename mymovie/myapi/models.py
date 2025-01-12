from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    #fields for the movie table
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    genre = models.CharField(max_length=100)
    created_at = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image=models.URLField(default='none', null=True)
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Review(models.Model):
    #fields for the review table
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username