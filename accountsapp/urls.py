from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import registration_view,MemberViewset,logout_view
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
   
    path('register/', registration_view, name="register"),
    path('login/',obtain_auth_token, name="login"),
    path('logout/',logout_view, name="logout"),
]


router = routers.SimpleRouter()
router.register("", MemberViewset, basename="accounts")
urlpatterns += router.urls


