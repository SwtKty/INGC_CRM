from django.db import models

# Create your models here.

class Employe(models.Model):
    prenomEmploye = models.CharField(max_length=200)
    nomEmploye = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
