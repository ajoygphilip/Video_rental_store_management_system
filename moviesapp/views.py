from django.shortcuts import render
from .models import Movie, MovieCopy
from rest_framework import viewsets
from .serializers import MovieSerializer, MovieCopyReadSerializer, MovieCopyWriteSerializer

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCopyViewset(viewsets.ModelViewSet):
    queryset = MovieCopy.objects.all()
    

    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return MovieCopyWriteSerializer
        return MovieCopyReadSerializer