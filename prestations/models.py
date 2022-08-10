from django.db import models
from clients.models import Client
from employes.models import Employe
from django.contrib.auth.models import User
from users.models import NewUser
from datetime import datetime


# Create your models here.
class Prestation(models.Model):

    STATUT_CHOICES = [
        ("EN_COURS", "EN_COURS"),
        ("FINI", "FINI"),
        ("VERIFIER", "VERIFIER"),
    ]

    nomPrestation = models.CharField(max_length=200)
    heureArrivee = models.TimeField(auto_now_add=True, null=True)
    heureDepart = models.TimeField(default=datetime.now().timetz(), null=True)
    ref_employe = models.ForeignKey(Employe, related_name='employe', null=True, on_delete=models.SET_NULL)
    ref_client = models.ForeignKey(Client, related_name='client', null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(default=datetime.now, null=True)
    commentaire = models.CharField(max_length=1000, blank=True)
    create_by = models.ForeignKey(NewUser, related_name='prestations', on_delete=models.CASCADE, null=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, null=True)
    remarque_client = models.CharField(max_length=1000, blank=True)


    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.nomPrestation



