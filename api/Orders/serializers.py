from rest_framework import serializers
from .models import Orders, DishOrder


class OrdersSerializer(serializers.ModelSerializer):
    """
    Orders Serializer
    """

    class Meta:
        model = Orders
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)


class DishOrderSerializer(serializers.ModelSerializer):
    """
    Dish Order Serializer
    """

    class Meta:
        model = DishOrder
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
