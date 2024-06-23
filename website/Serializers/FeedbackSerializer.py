from rest_framework import serializers

from website.Models.FeedbackModel import Feedback
from website.Serializers.StudentSerializer import StudentSerializer


class FeedbackSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'
