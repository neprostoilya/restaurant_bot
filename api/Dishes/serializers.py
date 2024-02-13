from rest_framework import serializers
from .models import Dishes


class DishesSerializer(serializers.ModelSerializer):
    """
    Dishes Serializer
    """
    class Meta:
        model = Dishes
        fields = ('pk', 'title', 'category', 'image', 'descriptiontrim', 'description', 'price')