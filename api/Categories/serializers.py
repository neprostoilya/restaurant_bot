from rest_framework import serializers
from Categories.models import Categories, Subategories

class CategoriesSerializer(serializers.ModelSerializer):
    """
    Categories Serializer
    """
    class Meta:
        model = Categories
        fields = '__all__'

class SubategoriesSerializer(serializers.ModelSerializer):
    """
    Subategories Serializer
    """
    class Meta:
        model = Subategories
        fields = '__all__'