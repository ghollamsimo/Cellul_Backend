from rest_framework import serializers

from website.Models.AppointementModel import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'