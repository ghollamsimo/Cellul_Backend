from rest_framework import serializers

from website.Models.EventModel import Event
from website.Serializers.MediaSerializer import MediaSerializer
from website.Serializers.UserSerializer import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True, read_only=True, source='media_set')
    user = UserSerializer(many=True, read_only=True, source='user_set')

    class Meta:
        model = Event
        fields = '__all__'
