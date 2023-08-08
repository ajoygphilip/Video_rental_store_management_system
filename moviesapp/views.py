from django.shortcuts import render
from .models import Movie
from rest_framework import viewsets
from .serializers import MovieSerializer

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer