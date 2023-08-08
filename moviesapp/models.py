from django.db import models

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