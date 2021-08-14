from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)
    category = models.CharField(max_length=10, blank = True, null = True)
    instructions = models.CharField(max_length=4000, blank = True, null = True)
    region = models.CharField(max_length=20, blank = True, null = True)
    slug = models.SlugField(default = 'test')
    image_url = models.CharField( max_length=50, blank = True, null = True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50, blank = True, null = True)
    year = models.CharField(max_length=4, blank = True, null = True)
    imdbID = models.CharField(max_length=20, blank = True, null = True)
    movie_type = models.CharField(max_length=50, blank = True, null = True)
    poster = models.CharField(max_length=500, blank = True, null = True)
    trailer = models.CharField(max_length=500, blank = True, null = True)
    rating = models.CharField(max_length=200, blank = True, null = True)
    runtime = models.CharField(max_length=10, blank = True, null = True)
    genre = models.CharField(max_length=50, blank = True, null = True)
    writer = models.CharField(max_length=50, blank = True, null = True)
    director = models.CharField(max_length=50, blank = True, null = True)
    cast = models.CharField(max_length=500, blank = True, null = True)
    plot = models.CharField(max_length=1000, blank = True, null = True)
    language = models.CharField(max_length=20, blank = True, null = True)
    def __str__(self):
        return self.title
    
class SearchedWord(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    savedMovies = models.JSONField(null = True, blank=True)
    def __str__(self):
        return self.user.username

