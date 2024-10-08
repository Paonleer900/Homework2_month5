from rest_framework import generics
from .models import Movie, Director
from Movie import MovieListView, DirectorListView

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.prefetch_related('reviews').all()
    serializer_class = MovieListView


class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorListView
