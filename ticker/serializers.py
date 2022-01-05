from rest_framework import serializers
from .models import Eth, Shib

class EthSerializer(serializers.ModelSerializer):
    class Meta:
        model=Eth
        fields=(
            'id',
            'pair',
            'price',
            'date'
        )

class ShibSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shib
        fields=(
            'id',
            'pair',
            'price',
            'date'
        )