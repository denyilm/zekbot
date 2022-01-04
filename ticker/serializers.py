from rest_framework import serializers
from .models import Eth

class EthSerializer(serializers.ModelSerializer):
    class Meta:
        model=Eth
        fields=(
            'id',
            'price',
            'date'
        )