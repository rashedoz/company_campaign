#event serializer

from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        
        fields = ('event_heading','event_date','event_details','event_banner')