from rest_framework import serializers
from .models import Movie, MovieCopy, RentedMovie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')



class MovieCopySerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='movie.title')
    class Meta:
        model = MovieCopy
        fields = ('id','title','movie','is_rented')



class RentedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentedMovie
        fields = ('__all__')