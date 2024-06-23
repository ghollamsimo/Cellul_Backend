from rest_framework import serializers

from website.Models.CalendarModel import Calendar


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'