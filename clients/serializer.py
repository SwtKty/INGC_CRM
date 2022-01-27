from rest_framework import serializers
from .models import Client


class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['prenomClient', 'nomClient', 'ageClient', 'emailClient',
                  'telClient', 'rueClient', 'villeClient', 'cpClient']
