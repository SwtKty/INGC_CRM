from django.db import models

# Create your models here.

class Client(models.Model):
    prenomClient = models.CharField(max_length=200, null=True)
    nomClient = models.CharField(max_length=200, null=True)
    ageClient = models.IntegerField(null=True)
    emailClient = models.CharField(max_length=200, null=True)
    adresseClient = models.CharField(max_length=600, null=True)

