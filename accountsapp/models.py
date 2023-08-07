from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
   
    def __str__(self):
        return self.user.username