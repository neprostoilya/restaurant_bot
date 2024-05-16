from rest_framework import serializers
from .models import Orders, DishOrder


class OrdersSerializer(serializers.ModelSerializer):
    """
    Orders Serializer
    """

    class Meta:
        model = Orders
        fields = ('pk', 'user', 'type_order', 'datetime_created', 'datetime_selected', 'total_quantity_all_dishes',
                    'place', 'people_quantity', 'total_price_all_dishes', 'status', 'longitude', 'latitude')
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
