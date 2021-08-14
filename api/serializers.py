from rest_framework import serializers
from main_app.models import Movie, Profile
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'year',
            'imdbID',
            'movie_type',
            'poster',
            'trailer',
            'rating',
            'runtime',
            'genre',
            'writer',
            'director',
            'cast',
            'plot',
            'language']

class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'year',
            'poster'
        ]


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    savedMovies = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin', 'savedMovies']

    def get_name(self, obj):
        name = obj.first_name
        if name =='':
            name = obj.email
        return name

    def get_isAdmin(self, obj):
        return obj.is_staff
    def get_savedMovies(self, obj):
        profile = Profile.objects.all().filter(user=obj)
        return profile[0].savedMovies

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin', 'token', 'savedMovies']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)