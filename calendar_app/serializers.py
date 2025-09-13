from rest_framework import serializers
from .models import Event, EventException

class EventExceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventException
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    exceptions = EventExceptionSerializer(many=True, read_only=True)  # nested exceptions

    class Meta:
        model = Event
        fields = '__all__'