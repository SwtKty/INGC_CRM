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


class prestationSerializer4(serializers.ModelSerializer):
    employe = employeSerializer3(many=False, read_only=True)
    client = clientSerializer3(many=False, read_only=True)
    class Meta:
        model = Prestation
        fields = ['employe', 'client']


class PrestationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = ['id', 'nomPrestation', 'heureArrivee', 'heureDepart', 'employe', 'client', 'commentaire']

    id = serializers.IntegerField(read_only=True)
    nomPrestation = serializers.CharField(required=True, allow_blank=False, max_length=100)
    employe = serializers.CharField(required=True, allow_blank=False, max_length=100)
    client = serializers.CharField(required=True, allow_blank=False, max_length=100)
    commentaire = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return Prestation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nomPrestation = validated_data.get('nomPrestation', instance.nomPrestation)
        instance.employe = validated_data.get('employe', instance.employe)
        instance.client = validated_data.get('client', instance.client)
        instance.save()
        return instance

