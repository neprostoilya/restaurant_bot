from rest_framework import serializers
from .models import Events


class EventsSerializer(serializers.ModelSerializer):
    """
    Events Serializer
    """
    class Meta:
        model = Events
        fields = '__all__'