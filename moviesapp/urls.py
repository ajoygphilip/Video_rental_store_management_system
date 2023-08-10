from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import MovieViewset, MovieCopyViewset, RentedMovieViewset, RentedMovieHistoryViewset, returnmovie

router = routers.SimpleRouter()

router.register("inventory", MovieCopyViewset, basename="movie-inventory")
router.register("rented/history", RentedMovieHistoryViewset,
                basename="rental-record-history")
router.register("rented", RentedMovieViewset, basename="current-rental-record")
router.register("catalouge", MovieViewset, basename="movies-catalouge")

urlpatterns = router.urls

urlpatterns += [path("return/", returnmovie, name="return-movie")]
