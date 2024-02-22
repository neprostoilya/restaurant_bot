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
        fields = ('pk', 'user', 'dish', 'quantity', 'get_dish_title', 'get_dish_price', 'get_quantity',
                  'get_dish_image', 'get_total_price', 'get_dish_pk')
        

class DeleteCartSerializer(serializers.Serializer):
    """
    Delete Cart Serializer
    """
    
    pk = serializers.CharField(
    )
    
