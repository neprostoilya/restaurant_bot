from rest_framework import serializers
from Orders.models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    """
    Orders Serializer
    """
    class Meta:
        model = Orders
        fields = ('pk', 'user', 'dish', 'completed')
        
    def create(self, validated_data):
        return super().create(validated_data)