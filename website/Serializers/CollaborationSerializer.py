from rest_framework import serializers

from website.Models.CollaborationModel import Collaboration


class CollaborationSerializer(serializers.Serializer):
    class Meta:
        model = Collaboration
        fields = '__all__'