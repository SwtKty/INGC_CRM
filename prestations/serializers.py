from rest_framework import serializers
from .models import Prestation


class prestationSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = '__all__'


class prestationSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = ['nomPrestation', 'employe', 'client']


class prestationSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = ['nomPrestation', 'heureArivee', 'heureDepart', 'employe', 'client']


class prestationSerializer4(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = ['heureDepart']



