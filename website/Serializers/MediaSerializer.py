from rest_framework import serializers

from website.Models.MediaModel import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'