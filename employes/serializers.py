from rest_framework import serializers
from .models import Employe


class employeSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ['prenomEmploye', 'nomEmploye', 'emailEmploye', 'telEmploye']


class employeSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'


class employeSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ['prenomEmploye', 'nomEmploye']


