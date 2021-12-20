from django.db import models

# Create your models here.
class Prestation(models.Model):
    nomPrestation = models.CharField(max_length=200)
    heureArrivee = models.TimeField
    heureDepart = models.TimeField
