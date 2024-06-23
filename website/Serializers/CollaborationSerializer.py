from rest_framework import serializers

from website.Models.CollaborationModel import Collaboration


class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = '__all__'