from rest_framework import serializers

from website.Models.CalendarModel import Calendar


class CalendarSerializer(serializers.Serializer):
    class Meta:
        model = Calendar
        fields = '__all__'