from django.db import models

# Create your models here.

class Employe(models.Model):
    prenomEmploye = models.CharField(max_length=200, null=True)
    nomEmploye = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
