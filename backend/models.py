from django.db import models
from datetime import datetime


# Create your models here.


class UserData(models.Model):
    page_url = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    browser = models.CharField(max_length=30)
    screen_resolution = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)
    browser_version = models.CharField(max_length=50, blank=True)
    os = models.CharField(max_length=50, blank=True)
    currency = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    latitude = models.CharField(max_length=50, blank=True)
    longitude = models.CharField(max_length=50, blank=True)
    os_version = models.CharField(max_length=50, blank=True)
    platform_type = models.CharField(max_length=50, blank=True)
    platform_vendor = models.CharField(max_length=50, blank=True)

    REQUIRED_FIELDS = ['user']
