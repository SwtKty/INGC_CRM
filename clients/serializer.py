from rest_framework import serializers
from .models import Client
from prestations.models import Prestation
from employes.models import Employe
from employes.employeSerializers import employeSerializer3


class clientSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['prenomClient', 'nomClient', 'ageClient', 'emailClient',
                  'telClient', 'rueClient', 'villeClient', 'cpClient']


class clientSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class clientSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['prenomClient', 'nomClient', 'rueClient', 'villeClient', 'cpClient']


class clientSerializer4(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['prenomClient']


class clientJobsSerializer(serializers.ModelSerializer):

    employe = employeSerializer3(many=False, read_only=True)
    client = clientSerializer3(many=False, read_only=True)

    class Meta:
        model = Prestation
        fields = '__all__'

    created = serializers.DateTimeField(read_only=True)
