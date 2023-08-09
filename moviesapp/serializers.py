from rest_framework import serializers
from .models import Movie, MovieCopy, RentedMovie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')

class MovieCopyWriteSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = MovieCopy
        fields = ('__all__')


class MovieCopyReadSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='movie.title')
   
    class Meta:
        model = MovieCopy
        fields = ('id', 'title')

class RentedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentedMovie
        fields = ('__all__')