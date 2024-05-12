from rest_framework import serializers

from website.Models.StudentModel import Student


class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = '__all__'
