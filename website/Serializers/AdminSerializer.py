from rest_framework import serializers

from website.Models.AdminModel import Admin
from website.Serializers.UserSerializer import UserSerializer


class AdminSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Admin
        fields = '__all__'
