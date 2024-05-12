from rest_framework import serializers

from website.Models.AdviseModel import Advise


class AdviseSerializer(serializers.Serializer):
    class Meta:
        model = Advise
        fields = '__all__'
