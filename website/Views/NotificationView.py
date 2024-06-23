from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from website.Serializers.NotificationSerializer import NotificationSerializer
from website.Services.NotificationService import NotificationService


class NotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, action=None):
        if action == 'delete_notification':
            return self.destroy_event(request, pk)
        if action == 'delete_notification_advise':
            return self.destroy_appointment(request, pk)
        else:
            return JsonResponse({'message': 'Method not allowed'}, status=405)

    def get(self, request, action=None):
        if action == 'get_notification':
            return self.index(request)

    def index(self, request):
        notification_service = NotificationService()
        notifications = notification_service.index(request)
        serializer = NotificationSerializer(notifications, many=True, context={'request': request})
        return Response({'notifications': serializer.data})

    def destroy_event(self, request, pk=None):
        if pk is not None:
            notification_service = NotificationService()
            notification_service.destroy_event_notification(request, pk=pk)
            return JsonResponse({'message': 'Notification deleted'}, status=200)
        else:
            return JsonResponse({'message': 'Bad Request: Missing "pk"'}, status=400)

    def destroy_appointment(self, request, pk=None):
        if pk is not None:
            notification_service = NotificationService()
            notification_service.destroy_appointment_notification(request, pk=pk)
            return JsonResponse({'message': 'Notification deleted'}, status=200)
        else:
            return JsonResponse({'message': 'Bad Request: Missing "pk"'}, status=400)
