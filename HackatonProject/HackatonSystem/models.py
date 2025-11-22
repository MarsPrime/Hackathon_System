from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    femail = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128)
    phone = models.IntegerField(max_length=11)
    email = models.EmailField()

    login = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

class Group(models.Model):
    name = models.CharField(max_length=128)
    event = models.IntegerField()

class Event(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    place = models.TextField()
    date = models.DateField()
