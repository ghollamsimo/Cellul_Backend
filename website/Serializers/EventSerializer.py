from rest_framework import serializers

from website.Models.EventModel import Event


class EventSerializer(serializers.Serializer):
    class Meta:
        model = Event
        fields = '__all__'
