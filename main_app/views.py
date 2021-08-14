from django.shortcuts import render
import requests
from .models import Food,Movie
# Create your views here.

def show_movies(request):
    foods = []
    if request.method == "GET":
        searchWord = request.GET.get('movie',False)
        if searchWord == False:
            return render( request, 'main_app/show_movies.html', {"searchWord":searchWord})
        else:
            url = "http://www.omdbapi.com/?s="+searchWord+"&apikey=62466339"
            response = requests.get(url)
            data = response.json()
            movies = data['Search']

            for i in movies :
                movie_sample = Movie(
                    title = i['Title'],
                    year = i['Year'],
                    imdbID = i['imdbID'],
                    movie_type = i['Type'],
                    poster = i['Poster'],
                    )
                try:
                    Movie.objects.get(title=movie_sample.title)
                except Movie.DoesNotExist:  
                    movie_sample.save()

                movies = Movie.objects.all().filter(title__icontains=searchWord)
            return render( request, 'main_app/show_movies.html', {"url":url, "movies":movies})
