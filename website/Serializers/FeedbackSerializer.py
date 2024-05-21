from rest_framework import serializers

from website.Models.FeedbackModel import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
