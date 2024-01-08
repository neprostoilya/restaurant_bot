from rest_framework import serializers
from Dishes.models import Dishes

class DishesSerializer(serializers.ModelSerializer):
    """
    Dishes Serializer
    """
    class Meta:
        model = Dishes
        fields = ('pk', 'title_ru', 'title_uz', 'description_ru', 'description_uz',
            'image', 'category', 'price', 'get_category_title_ru', 'get_category_title_uz')