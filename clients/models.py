from django.db import models

# Create your models here.

class Client(models.Model):
    prenomClient = models.CharField(max_length=200)
    nomClient = models.CharField(max_length=200)
    ageClient = models.IntegerField
    emailClient = models.CharField(max_length=200)
    adresseClient = models.CharField(max_length=600)

