from rest_framework import serializers
from .models import Prestation


class prestationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = '__all__'
