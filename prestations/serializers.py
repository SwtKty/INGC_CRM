from rest_framework import serializers

from clients.serializer import clientSerializer1, clientSerializer3
from employes.serializers import employeSerializer1, employeSerializer3
from .models import Prestation
from .models import Client
from .models import Employe


class prestationSerializer1(serializers.ModelSerializer):
    employe = employeSerializer3(many=False, read_only=True)
    client = clientSerializer3(many=False, read_only=True)
    class Meta:
        model = Prestation
        fields = '__all__'


class prestationSerializer3(serializers.ModelSerializer):
    employe = employeSerializer3(many=False, read_only=True)
    client = clientSerializer3(many=False, read_only=True)
    class Meta:
        model = Prestation
        fields = ['nomPrestation', 'employe', 'client']


class prestationSerializer2(serializers.ModelSerializer):
    employe = employeSerializer3(many=False, read_only=True)
    client = clientSerializer3(many=False, read_only=True)
    class Meta:
        model = Prestation
        fields = ['nomPrestation', 'heureArivee', 'heureDepart', 'employe', 'client']


class prestationSerializer4(serializers.ModelSerializer):
    employe = employeSerializer3(many=False, read_only=True)
    client = clientSerializer3(many=False, read_only=True)
    class Meta:
        model = Prestation
        fields = ['heureDepart']



