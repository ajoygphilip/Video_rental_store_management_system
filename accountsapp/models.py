from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)

    is_staff = models.BooleanField(default=False)

    @property
    def is_currently_renting(self):
        try:
            return True if self.user.rented_movies.filter(returned=False).count()>0 else False
        except:
            return False
    
   
    def __str__(self):
        return self.user.username