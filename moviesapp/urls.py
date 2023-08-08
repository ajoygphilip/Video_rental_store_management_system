from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import MovieViewset

router = routers.SimpleRouter()

router.register("", MovieViewset, basename="movies")


urlpatterns = router.urls
