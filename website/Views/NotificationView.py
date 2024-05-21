from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from website.Services.NotificationService import NotificationService


@api_view(['POST'])
def store_notification(request):
    if request.method == 'POST':
        notification_service = NotificationService()
        notification = notification_service.store_event_notification()
        return JsonResponse({'message': 'Notification Created successfully'})


@method_decorator(csrf_exempt, name='dispatch')
class NotificationView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, pk, action=None):
        if action == 'delete_notification':
            return self.destroy_event(request, pk)
        if action == 'delete_notification_advise':
            return self.destroy_appointment(request, pk)
        else:
            return JsonResponse({'message': 'Method not allowed'}, status=405)

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