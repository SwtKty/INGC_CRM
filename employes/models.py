from django.db import models


# Create your models here.

class Employe(models.Model):
    prenomEmploye = models.CharField(max_length=200, null=True)
    nomEmploye = models.CharField(max_length=200, null=True)
    emailEmploye = models.CharField(max_length=200, null=True)
    telEmploye = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.prenomEmploye)
