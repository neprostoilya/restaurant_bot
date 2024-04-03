from rest_framework import serializers
from .models import Dishes


class DishesSerializer(serializers.ModelSerializer):
    """
    Dishes Serializer
    """
    class Meta:
        model = Dishes
        fields = (
            'pk', 'title_ru', 'category', 'image', 'descriptiontrim_ru', 'description_ru', 'price',
            'title_uz', 'descriptiontrim_uz', 'description_uz', 
        )