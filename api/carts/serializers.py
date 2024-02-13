from rest_framework import serializers
from .models import Carts


class CartsSerializer(serializers.ModelSerializer):
    """
    Carts Serializer
    """
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    class Meta:
        model = Carts
        fields = ('pk', 'user', 'dish', 'amount')