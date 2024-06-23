from rest_framework import serializers

from website.Models.AdviseModel import Advise
from website.Serializers.UserSerializer import UserSerializer


class AdviseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Advise
        fields = '__all__'
