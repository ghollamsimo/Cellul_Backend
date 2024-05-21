from django.http import JsonResponse
from rest_framework.views import APIView

from website.Serializers.FeedbackSerializer import FeedbackSerializer
from website.Services.FeedbackService import FeedbackService


class FeedbackView(APIView):

    def post(self, request, advise, action=None):
        if request.method == 'POST':
            if action == 'add_feedback':
                return self.add_feedback(request, advise)
        pass

    def get(self, request, action=None):
        if request.method == 'GET':
            if action == 'all_feedback':
                return self.all_feedback(request)

    def put(self, request, pk, action=None):
        if request.method == 'PUT':
            if action == 'update_feedback':
                return self.update_feedback(pk, request.data)

    def delete(self, request, pk, student, action=None):
        if request.method == 'DELETE':
            if action == 'delete_feedback':
                return self.delete_feedback(pk, student)

    def add_feedback(self, request, advise):
        feedback_service = FeedbackService()
        feedback_service.store_feedback(request, advise)
        return JsonResponse({'message': 'Feedback added successfully'})
        pass

    def all_feedback(self, request):
        feedback_service = FeedbackService()
        feedback = feedback_service.index(request)
        feedback_serializer = FeedbackSerializer(feedback, many=True)
        return JsonResponse(feedback_serializer.data, status=200, safe=False)
        pass

    def update_feedback(self, pk, request):
        feedback_service = FeedbackService()
        feedback_service.update_feedback(pk, request)
        return JsonResponse({'meesage': 'Feedback updated successfully'})
        pass

    def delete_feedback(self, pk, student):
        feedback_service = FeedbackService()
        feedback_service.destroy_feedback(pk, student)
        return JsonResponse({'message': 'Feedback deleted successfully'})