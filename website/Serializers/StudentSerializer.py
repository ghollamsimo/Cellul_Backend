from rest_framework import serializers

from website.Models.StudentModel import Student
from website.Serializers.UserSerializer import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
