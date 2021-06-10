from django.db import models

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=64)
    city = models.CharField(max_length=64)


class People(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
