from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    api_key = models.CharField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['username', 'api_key']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return "{}".format(self.email)



