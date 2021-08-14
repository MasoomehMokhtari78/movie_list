import os
from requests_cache import CachedSession
import googleapiclient.discovery
from rest_framework import generics, permissions
from .serializers import MovieSerializer, SearchResultSerializer, UserSerializer, UserSerializerWithToken
from main_app.models import Movie, SearchedWord, Profile
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import requests
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
import json

# Create your views here.

class movieList(generics.ListAPIView):
    serializer_class = MovieSerializer
    

    def get_queryset(self):
        movies = Movie.objects.all()
        return movies

@api_view(['GET'])
def getMovies(request, name):
    # if the search result for this word has already been saved into the database
    try:
        SearchedWord.objects.get(name=name)

    except SearchedWord.DoesNotExist:  
        newSearch = SearchedWord(name=name)
        newSearch.save()
        url = "http://www.omdbapi.com/?s="+name+"&apikey=62466339"
        response = requests.get(url)
        # print(response)
        data = response.json()
        searchResults = data['Search']
        # movieData = []
        for result in searchResults:
            
            movieUrl = "http://www.omdbapi.com/?t="+result['Title']+"&apikey=62466339"
            response = requests.get(movieUrl)
            result = response.json()
            movie_sample = Movie(
                title = result['Title'],
                year = result['Year'],
                imdbID = result['imdbID'],
                movie_type = result['Type'],
                poster = result['Poster'],
                trailer = getTrailer(result['Title']),
                rating = result['Ratings'],
                runtime = result['Runtime'],
                genre = result['Genre'],
                writer = result['Writer'],
                director = result['Director'],
                cast = result['Actors'],
                plot = result['Plot'],
                language = result['Language']
                )
            try:
                Movie.objects.get(title=movie_sample.title)
            except Movie.DoesNotExist:  
                movie_sample.save()
    

    movies = Movie.objects.all().filter(title__icontains=name)

    serializer = SearchResultSerializer(movies, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def getMovieById(request, id):
    movie = Movie.objects.all().filter(id=id)
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMovieByGenre(request, genre):
    movie = Movie.objects.all().filter(genre__icontains=genre)
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def IMDBAPI(request, name):
    params = {
        'q':"pulp fiction",
        'k': "420413-Elle-H1XFYAQT",
        'type': 'movie'
    }
    url = 'https://tastedive.com/api/similar'
    # url = 'https://imdb-api.com/API/Search/k_x9fnbsut/' + name
    response = requests.get(url, params)
    data = response.json()

    return Response(page1)


def getTrailer(name):

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCibMfVGWZHKB0BeSnZ--bduRn-gExrhPY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=name + "official trailer"
    )
    response = request.execute()
    # print("this is video:")
    # print(response['items'][0]['id']['videoId'])
    videoId = response['items'][0]['id']['videoId']
    return videoId


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k,v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    # try:
    data = request.data
    user = User.objects.create(
        first_name=data['name'],
        username=data['email'],
        email=data['email'],
        password=make_password(data['password'])
    )
    # profile = Profile.objects.create(
    #     user = user,
    #     savedMovies = "{}"
    # )
    serializer = UserSerializerWithToken(user,many=False)
    return Response(serializer.data)
    # except:
        # message = {'detail':'User with this email already exists'}
        # return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMovie(request):
    userProfile = request.user.profile
    allMovies = userProfile.savedMovies
    # print(type(allMovies))
    data = request.data["addMovie"]
    print(data)
    # print(data[0]['id'])
    # dataDict = {}
    # movieId = data[0]['id']
    # dataDict[movieId] = {}
    # dataDict[movieId]['title'] = data[0]['title']
    # dataDict[movieId]['poster'] = data[0]['poster']
    # print(dataDict)
    # dataDict['id']['title'] = data[0]['title']
    # dataDict['id']['poster'] = data[0]['poster']
    json_data = json.loads(data)
    # print(json_data)
    # print(newMovie['name'])
    # print(allMovies)
    if(allMovies):
        print('here')
        allMovies.update(json_data)
    else:
        userProfile.savedMovies = json_data
    
    
    # # print(allMovies)
    userProfile.save()
    serializer = UserSerializerWithToken(request.user,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteMovie(request):
    userProfile = request.user.profile
    allMovies = userProfile.savedMovies
    data = request.data["deleteMovie"]
    # print(data)
    json_data = json.loads(data)
    keys = [*json_data]
    print(keys[0])
    allMovies.pop(keys[0])
    userProfile.save()
    serializer = UserSerializerWithToken(request.user,many=False)
    print(serializer.data)
    return Response(serializer.data)

