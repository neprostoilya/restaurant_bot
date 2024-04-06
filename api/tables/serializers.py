from rest_framework import serializers
from .models import Tables


class TablesSerializer(serializers.ModelSerializer):
    """
    Tables Serializer
    """
    class Meta:
        model = Tables
        fields = '__all__'