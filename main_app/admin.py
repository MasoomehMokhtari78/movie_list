from django.contrib import admin
from .models import Food, Movie, SearchedWord, Profile
# Register your models here.
admin.site.register(Food)
admin.site.register(Movie)
admin.site.register(SearchedWord)
admin.site.register(Profile)