# website/Serializers/NotificationSerializer.py
from rest_framework import serializers
from website.Models.NotificationModel import Notification
from website.Serializers.AdviseSerializer import AdviseSerializer
from website.Serializers.AppointmentSerializer import AppointmentSerializer
from website.Serializers.EventSerializer import EventSerializer
from website.Serializers.StudentSerializer import StudentSerializer


class NotificationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    appointment = AppointmentSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    advise = AdviseSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'

