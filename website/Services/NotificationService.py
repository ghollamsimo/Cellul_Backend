from django.http import JsonResponse

from website.Repository.Implementations.NotificationRepository import NotificationRepository


class NotificationService:
    def __init__(self):
        self.NotificationRepository = NotificationRepository()

    def store_event_notification(self):
        return self.NotificationRepository.store_of_event()

    def store_appointment_notification(self):
        return self.NotificationRepository.store_of_appointment()

    def destroy_event_notification(self, request, pk):
        self.NotificationRepository.destroy_of_event(request, pk)
        return JsonResponse({'message': 'Notification deleted successfully'})
        pass

    def destroy_appointment_notification(self, request, pk):
        self.NotificationRepository.destroy_of_appointment(request, pk)
        return JsonResponse({'message': 'Notification deleted successfully'})
        pass

    def index(self, request):
        return self.NotificationRepository.index(request)
        pass