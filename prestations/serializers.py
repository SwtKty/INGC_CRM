from rest_framework import serializers

from clients.serializer import clientSerializer1, clientSerializer3, clientSerializer4
from employes.serializers import employeSerializer1, employeSerializer3
from .models import Prestation
from .models import Client, Employe, NewUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class prestationSerializer1(serializers.ModelSerializer):
    employe = employeSerializer3(many=False, read_only=True)
    client = clientSerializer3(many=False, read_only=True)

    class Meta:
        model = Prestation
        fields = '__all__'

#class prestationSerializer3(serializers.ModelSerializer):
    employe = employeSerializer3(many=False, read_only=True)
    client = clientSerializer3(many=False, read_only=True)

    class Meta:
        model = Prestation
        fields = ['nomPrestation', 'employe', 'client']


class prestationSerializer4(serializers.ModelSerializer):
    employe = employeSerializer3(many=False, read_only=True)
    client = clientSerializer3(many=False, read_only=True)

    class Meta:
        model = Prestation
        fields = ['employe', 'client']


# nouvelle version commence ici


class UserSerializer(serializers.HyperlinkedModelSerializer):
    prestations = serializers.HyperlinkedRelatedField(many=True, view_name='prestations-detail', read_only=True)
    create_by = serializers.ReadOnlyField(source='create_by.username')

    class Meta:
        model = NewUser
        fields = ['create_by', 'id', 'user_name', 'prestations']


class PrestationSerializer(serializers.HyperlinkedModelSerializer):
    create_by = serializers.ReadOnlyField(source='create_by.username')
    prenomEmploye = Employe()
    prenomClient = Client()

    class Meta ():
        model = Prestation
        fields = ['create_by', 'id', 'nomPrestation', 'heureArrivee', 'heureDepart',
                  'commentaire', 'prenomEmploye', 'prenomClient']

    id = serializers.IntegerField(read_only=True)
    nomPrestation = serializers.CharField(required=True, allow_blank=False, max_length=100)
    prenomEmploye = employeSerializer3()
    prenomClient = clientSerializer4()
    commentaire = serializers.CharField(style={'base_template': 'textarea.html'})
    heureDepart = serializers.TimeField(required=False)

    def create(self, validated_data):
        return Prestation.objects.create(**validated_data)
