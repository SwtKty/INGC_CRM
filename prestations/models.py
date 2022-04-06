from django.db import models
from clients.models import Client
from employes.models import Employe


# Create your models here.
class Prestation(models.Model):
    nomPrestation = models.CharField(max_length=200)
    heureArrivee = models.TimeField(auto_now_add=True, null=True)
    heureDepart = models.TimeField(auto_now_add=True, null=True)
    employe = models.ForeignKey(Employe, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True, null=True)
    commentaire = models.CharField(max_length=1000, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.nomPrestation)
