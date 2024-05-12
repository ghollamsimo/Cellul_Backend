from rest_framework import serializers

from website.Models.AdminModel import Admin


class AdminSerializer(serializers.Serializer):
    class Meta:
        model = Admin
        fields = '__all__'
