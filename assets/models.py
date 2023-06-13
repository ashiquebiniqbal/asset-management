from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Asset(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    employee = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    checked_out_at = models.DateTimeField(null=True, blank=True)
    checked_in_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name



class Subscriber(AbstractBaseUser):
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Add other fields and methods as needed


  
  
  