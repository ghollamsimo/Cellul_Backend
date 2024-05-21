from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes

from django.http import JsonResponse
from rest_framework import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication

from website.Models.AdminModel import Admin
from website.Services.EventService import EventService
from website.Services.NotificationService import NotificationService
from website.Serializers.EventSerializer import EventSerializer


@method_decorator(csrf_exempt, name='dispatch')
class EventView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, action=None):
        if action == 'add_event':
            return self.create(request)
        elif action == 'update_event':
            pk = request.data.get('pk')
            return self.update(request, pk)
        elif action == 'delete_event':
            pk = request.data.get('pk')
            return self.delete(request, pk)
        elif action == 'all_events':
            return self.get(request)
        else:
            return JsonResponse({'message': 'Invalid action'}, status=400)

    def create(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        localisation = request.data.get('localisation')
        user_id = request.data.get('user_id')

        if not (title and description and start_time and end_time and localisation):
            return JsonResponse({'message': 'Please fill in all fields'}, status=400)

        try:
            admin = Admin.objects.get(user=user_id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError("Admin for the user does not exist")

        try:
            event_repository = EventService()
            event_repository.store(request.data, admin)
            notification_service = NotificationService()
            notification_service.store_event_notification()
            return JsonResponse({'message': 'Event created successfully'}, status=201)
        except serializers.ValidationError as e:
            return JsonResponse({'message': 'Validation error', 'details': e.detail}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'An error occurred', 'details': str(e)}, status=500)

    def update(self, request, pk):
        title = request.data.get('title')
        description = request.data.get('description')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        localisation = request.data.get('localisation')

        if not (title and description and start_time and end_time and localisation):
            return JsonResponse({'message': 'Please fill in all fields'}, status=400)

        try:
            event_service = EventService()
            updated_event = event_service.update(pk, {
                'title': title,
                'description': description,
                'start_time': start_time,
                'end_time': end_time,
                'localisation': localisation
            })
            serializer = EventSerializer(updated_event)
            return JsonResponse({'message': 'Event updated successfully', 'event': serializer.data}, status=200)
        except serializers.ValidationError as e:
            return JsonResponse({'message': 'Validation error', 'details': e.detail}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'An error occurred', 'details': str(e)}, status=500)

    def get(self, request):
        event_service = EventService()
        events = event_service.index(request)
        serializer = EventSerializer(events, many=True)
        return Response({'events': serializer.data}, status=200)

    def delete(self, request, pk):
        try:
            event_service = EventService()
            event_service.destroy(pk=pk)
            return Response({'message': 'Event deleted successfully'}, status=200)
        except Exception as e:
            return Response({'message': 'An error occurred', 'details': str(e)}, status=500)