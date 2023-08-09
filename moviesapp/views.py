from django.shortcuts import render
from .models import Movie, MovieCopy, RentedMovie
from rest_framework import viewsets, status
from .serializers import MovieSerializer, MovieCopyReadSerializer, MovieCopyWriteSerializer, RentedMovieSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['post'])
    def rent(self, request, pk=None):
        
        if request.user.profile.is_currently_renting:
            return Response({'message': 'You have already rented a Movie. Please return it to rent another one.'},
                            status=status.HTTP_400_BAD_REQUEST)

        available_copies = self.get_object().copies.filter(is_rented=False)
        
        if available_copies.count()<1:
            return Response({'message': 'No DVDs available for this movie. Please try after some days or try a different movie'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            copy=available_copies[0]
            new_rental_record = RentedMovie(moviecopy=copy,customer=request.user)
            new_rental_record.save()
            copy.is_rented=True
            copy.save()

            return Response({'message': 'Rental Succesful'},
                                status=status.HTTP_200_OK)

class MovieCopyViewset(viewsets.ModelViewSet):
    queryset = MovieCopy.objects.all()
    

    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return MovieCopyWriteSerializer
        return MovieCopyReadSerializer
    
class RentedMovieViewset(viewsets.ModelViewSet):
    queryset = RentedMovie.objects.all()
    serializer_class = RentedMovieSerializer