from rest_framework import serializers

from website.Models.AppointementModel import Appointment
from website.Serializers.AdviseSerializer import AdviseSerializer
from website.Serializers.StudentSerializer import StudentSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    advise = AdviseSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'