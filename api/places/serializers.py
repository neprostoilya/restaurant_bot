from rest_framework import serializers
from .models import Places


class PlacesSerializer(serializers.ModelSerializer):
    """
    Places Serializer
    """
    class Meta:
        model = Places
        fields = '__all__'