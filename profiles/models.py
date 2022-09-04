from django.db import models
from django.db.models import CharField, ImageField, TextField, IntegerField

# Create your models here.


class plants(models.Model):

    Pname = models.CharField(max_length=100)
    PCount = models.IntegerField()


class garden(models.Model):

    Pname = models.CharField(max_length=100)
    PDetails = models.TextField()
    username = models.CharField(max_length=100)
