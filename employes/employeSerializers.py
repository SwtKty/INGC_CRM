from rest_framework import serializers
from .models import Employe
from clients.models import Client
from django.contrib.auth.models import User
from prestations.models import Prestation


class EmployeLoginSerializer (serializers.ModelSerializer):

    class Meta:
        model = Employe
        fields = ['emailEmploye','mdpEmploye','token']

        read_only_fields = ['token']


class employeSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ['prenomEmploye', 'nomEmploye', 'emailEmploye', 'telEmploye']


class employeSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'


class employeClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class employeSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ['prenomEmploye']


class employeJobsSerializer(serializers.ModelSerializer):

    employe = employeSerializer3(many=False, read_only=True)
    client = employeClientSerializer(many=False, read_only=True)

    class Meta:
        model = Prestation
        fields = '__all__'

    created = serializers.DateTimeField(read_only=True)
