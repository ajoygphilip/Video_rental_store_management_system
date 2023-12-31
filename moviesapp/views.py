from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Movie, MovieCopy, RentedMovie
from .permissions import IsStaff, IsStaffOrReadOnly
from .serializers import (
    MovieCopySerializer,
    MovieSerializer,
    RentedMovieHistorySerializer,
    MovieCopyWriteSerializer,
    RentedMovieSerializer,
)


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsStaffOrReadOnly,)

    @action(detail=True, methods=["get"], permission_classes=(IsAuthenticated, IsStaff))
    def inventory(self, request, pk=None):
        query = MovieCopy.objects.filter(movie__id=pk)
        serializer = MovieCopySerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], permission_classes=(IsAuthenticated,))
    def rent(self, request, pk=None):
        if request.user.profile.is_currently_renting:
            return Response(
                {
                    "message": "You have already rented a Movie. Please return it to rent another one."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        available_copies = self.get_object().copies.filter(is_rented=False)

        if available_copies.count() < 1:
            return Response(
                {
                    "message": "No DVDs available for this movie. Please try after some days or try a different movie"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            copy = available_copies[0]
            new_rental_record = RentedMovie(
                moviecopy=copy, customer=request.user)
            new_rental_record.save()
            copy.is_rented = True
            copy.save()

            return Response({"message": "Rental Succesful"}, status=status.HTTP_200_OK)


@api_view(["POST",])
@permission_classes((IsAuthenticated,))
def returnmovie(request):
    if not request.user.profile.is_currently_renting:
        return Response(
            {"message": "You have no pending returns"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    else:
        rental_record = request.user.rented_movies.filter(returned=False)[
            0]
        fine_amount = rental_record.fine_amount
        rental_record.returned = True
        rental_record.save()

        copy = rental_record.moviecopy
        copy.is_rented = False
        copy.save()
        return Response({"message": "Movie returned", "fine_amount": fine_amount}, status=status.HTTP_200_OK)


class MovieCopyViewset(viewsets.ModelViewSet):
    queryset = MovieCopy.objects.all()
    permission_classes = (IsStaff,)
    serializer_class = MovieCopySerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieCopySerializer
        else:
            return MovieCopyWriteSerializer


class RentedMovieViewset(viewsets.ModelViewSet):
    serializer_class = RentedMovieSerializer
    permission_classes = (IsAuthenticated, IsStaffOrReadOnly)

    def get_queryset(self):
        if self.request.user.profile.is_staff:
            return RentedMovie.objects.filter(returned=False)
        else:
            return self.request.user.rented_movies.filter(returned=False)


class RentedMovieHistoryViewset(viewsets.ModelViewSet):
    serializer_class = RentedMovieHistorySerializer
    permission_classes = (IsAuthenticated, IsStaffOrReadOnly)

    def get_queryset(self):
        if self.request.user.profile.is_staff:
            return RentedMovie.objects.all()
        else:
            return self.request.user.rented_movies.all()
