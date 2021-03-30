# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    license_number = models.CharField(max_length=20, unique=True)
    car_number = models.CharField(max_length=15, unique=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    row_created = models.DateTimeField(auto_now_add=True)
    row_last_updated = models.DateTimeField(auto_now=True)
