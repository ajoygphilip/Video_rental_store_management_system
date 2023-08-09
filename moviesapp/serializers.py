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


class MovieCopySerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='movie.title')

    rented_by = serializers.SerializerMethodField('get_rented_by')

    def get_rented_by(self, obj):
        try:
            return str(obj.transfers.filter(returned=False)[0].customer)
        except:
            return None

    class Meta:
        model = MovieCopy
        fields = ('id', 'title', 'movie', 'is_rented', "rented_by")


class RentedMovieSerializer(serializers.ModelSerializer):
    fine_amount = serializers.ReadOnlyField()
    due_date = serializers.ReadOnlyField()

    class Meta:
        model = RentedMovie
        fields = ('__all__')


class RentedMovieHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RentedMovie
        fields = ('__all__')
