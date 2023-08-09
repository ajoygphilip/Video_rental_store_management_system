from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import MovieViewset, MovieCopyViewset, RentedMovieViewset,RentedMovieHistoryViewset

router = routers.SimpleRouter()

router.register("copies", MovieCopyViewset, basename="moviecopies")
router.register("rented/history", RentedMovieHistoryViewset, basename="rentalrecord")
router.register("rented", RentedMovieViewset, basename="rentalrecord")
router.register("", MovieViewset, basename="movies")


urlpatterns = router.urls
