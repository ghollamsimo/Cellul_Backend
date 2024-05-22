from rest_framework import serializers

from website.Models.RecordsModel import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'