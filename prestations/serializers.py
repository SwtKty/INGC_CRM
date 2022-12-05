import datetime

from rest_framework import serializers

from clients.serializer import clientSerializer1, clientSerializer3, clientSerializer4
from employes.employeSerializers import employeSerializer1, employeSerializer3
from .models import Prestation
from .models import Client, Employe, NewUser
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Group
        fields = ['url', 'name']



class prestationSerializer1(serializers.ModelSerializer):
    employe = employeSerializer3(many=False, read_only=True)
    client = clientSerializer3(many=False, read_only=True)

    class Meta:
        model = Prestation
        fields = '__all__'

    created = serializers.DateTimeField(read_only=True)


class prestationSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = ['commentaire', 'heureDepart']

    heureDepart = serializers.TimeField(read_only=True)


class UserSerializer2(serializers.HyperlinkedModelSerializer):
    prestations = serializers.HyperlinkedRelatedField(many=True, view_name='prestations-detail', read_only=True)
    create_by = serializers.ReadOnlyField(source='create_by.username')

    class Meta:
        model = NewUser
        fields = ['create_by', 'id', 'user_name', 'prestations']


class prestationSerializer5(serializers.ModelSerializer):
    create_by = serializers.ReadOnlyField(source='create_by.username')

    class Meta():
        model = Prestation
        fields = '__all__'

    id = serializers.IntegerField(read_only=True)
    nomPrestation = serializers.CharField(required=True, allow_blank=False, max_length=100)
    heureArrivee = serializers.DateTimeField(read_only=True)
    commentaire = serializers.CharField(style={'base_template': 'textarea.html'})
