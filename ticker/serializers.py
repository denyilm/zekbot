from rest_framework import serializers
from .models import Balance, Eth, Shib, Transaction

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

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Balance
        fields=(
            'id',
            'eth',
            'shib',
            'para'
            'date'
        )

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=(
            'id',
            'type',
            'pair',
            'price',
            'profit',
            'date'
        )