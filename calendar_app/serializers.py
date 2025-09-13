from rest_framework import serializers
from .models import Event, EventException

class EventExceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventException
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate(self, data):
        event_type = data.get('event_type')
        meeting_type = data.get('meeting_type')
        host = data.get('host')
        location = data.get('location')

        if event_type == 'MEETING' and not meeting_type:
            raise serializers.ValidationError("Meeting type must be set for Meeting events.")
        if event_type in ['1ST_APPOINTMENT', 'PRESENTATION'] and not host:
            raise serializers.ValidationError("Host must be set for Appointment or Presentation events.")
        if event_type == 'EVENT' and not location:
            raise serializers.ValidationError("Location must be set for Event type.")
        return data