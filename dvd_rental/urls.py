from django.contrib import admin
from django.urls import path, include
from accountsapp.views import registration_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accountsapp.urls")),
    path('movies/', include("moviesapp.urls")),

]
