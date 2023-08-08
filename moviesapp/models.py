from django.db import models
from accountsapp.models import Profile
from datetime import datetime, timedelta


# Create your models here.
class Movie(models.Model):
    '''This model represents one movie and stores related details.'''
    GENRE_CHOICES = (
    ('action','Action'),
    ('drama','Drama'),
    ('comedy','Comedy'),
    ('horror','Horror'),
    ('thriller','Thriller'),
    ('romance','Romance'),
)
    title = models.CharField(max_length=200)
    description = models.TextField() 
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)

    def __str__(self):
        return f"{self.title} ({self.release_year})"
    

class MovieCopy(models.Model):
    '''Represents one physical copy of a movie in the store'''
    movie = models.ForeignKey(
        Movie, verbose_name="Movie Copy", related_name='copies', on_delete=models.CASCADE)
    

    