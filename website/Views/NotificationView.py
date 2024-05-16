from django.http import JsonResponse
from rest_framework.decorators import api_view

from website.Services.NotificationService import NotificationService


@api_view(['GET'])
def store_notification(request):
    if request.method == 'GET':
        notification_service = NotificationService()
        notification = notification_service.store_event_notification()
        return JsonResponse({'message': 'Notification Created successfully'})