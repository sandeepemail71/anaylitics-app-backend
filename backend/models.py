from django.db import models
from datetime import datetime


# Create your models here.


class UserData(models.Model):
    page_url = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    browser = models.CharField(max_length=30)
    screen_resolution = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['user']
