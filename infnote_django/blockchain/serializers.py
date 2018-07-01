from rest_framework import serializers

from posts.serializers import PostSerializer as BasePostSerializer, TimestampField

from .models import *


class BaseCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = '__all__'


class BaseTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class CoinSerializer(BaseCoinSerializer):
    class Meta:
        model = Coin
        fields = ('txid', 'vout', 'value')


class PostSerializer(BasePostSerializer):
    date_confirmed = TimestampField()
    user = None

    class Meta(BasePostSerializer.Meta):
        read_only_fields = (
            'id', 'user',
            'views', 'replies', 'last_reply'
        )
