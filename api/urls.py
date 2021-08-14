from django.urls import path
from . import views


urlpatterns = [
    path('users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.movieList.as_view()),
    path('searchResults/<str:name>', views.getMovies),
    path('movies/<str:id>', views.getMovieById),
    path('genre/<str:genre>', views.getMovieByGenre),
    path('imdbMovies/<str:name>', views.IMDBAPI),
    path('users/profile/', views.getUserProfile),
    path('users/', views.getUsers),
    path('users/register', views.registerUser),
    path('users/addMovie', views.addMovie),
    path('users/deleteMovie', views.deleteMovie),
    # path('trailer/<str:name>',views.getTrailer)
] 
