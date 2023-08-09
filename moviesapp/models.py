from django.db import models
from accountsapp.models import Profile
from datetime import datetime, timedelta
from django.contrib.auth.models import User

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

    @property
    def total_copies_count(self):
        return self.copies.count()

    @property
    def rented_copies_count(self):
        copies = self.copies.all()
        rented_copies = [copy.transfers.filter(
            returned=False) for copy in copies if copy.transfers.filter(
            returned=False).count()]

        return len(rented_copies)

    @property
    def available_copies_count(self):
        available_copies_count = self.total_copies_count - self.rented_copies_count
        return available_copies_count

    def __str__(self):
        return f"{self.title} ({self.release_year})"
    

class MovieCopy(models.Model):
    '''Represents one physical copy of a movie in the store'''
    movie = models.ForeignKey(
        Movie, verbose_name="Movie Copy", related_name='copies', on_delete=models.CASCADE)
    is_rented = models.BooleanField(default=False)
    
    
class RentedMovie(models.Model):
    '''Represents the rental  of one MovieCopy to one customer'''

    moviecopy = models.ForeignKey(
        MovieCopy, on_delete=models.CASCADE, related_name='transfers')

    customer = models.ForeignKey(
        User,
        verbose_name="Rented by",
        on_delete=models.CASCADE,
        related_name="rented_movies")

    rented_date = models.DateField(
        verbose_name="Rented On",
        auto_now=True)

    returned = models.BooleanField(default=False)

    @ property
    def due_date(self):
        return self.rented_date + timedelta(days=14)

    @ property
    def fine_amount(self):
        fine_per_day_for_first_week = 5
        fine_per_day_from_week_two = 10

        if datetime.today().date() <= self.due_date:
            return 0

        number_of_days_late = (datetime.today().date() - self.due_date).days

        if number_of_days_late <= 7:
            return fine_per_day_for_first_week * number_of_days_late
        
        else:
            first_week_fine = fine_per_day_for_first_week * 7 
            subsequent_week_fine = fine_per_day_from_week_two * (number_of_days_late - 7) 

            return first_week_fine + subsequent_week_fine

    def __str__(self):
        return f"{self.moviecopy.movie} CopyID {self.id} rented to {self.customer}"
    