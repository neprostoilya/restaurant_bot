from rest_framework import serializers
from Orders.models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    """
    Orders Serializer
    """
    class Meta:
        model = Orders
        fields = '__all__'
        
    def create(self, validated_data):
        return super().create(validated_data)