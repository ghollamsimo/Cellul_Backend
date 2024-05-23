from rest_framework import serializers

from website.Models.EventModel import Event
from website.Serializers.MediaSerializer import MediaSerializer


class EventSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
