from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication

from website.Models.AdminModel import Admin
from website.Services.EventService import EventService
from website.Services.NotificationService import NotificationService
from website.Serializers.EventSerializer import EventSerializer


@method_decorator(csrf_exempt, name='dispatch')
class EventView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, action=None):
        if action == 'add_event':
            return self.create(request=request)
        else:
            return JsonResponse({'message': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, action=None):
        if action == 'delete_event':
            return self.delete_event(pk, request)

    def put(self, request, pk, action=None):
        if action == 'update_event':
            return self.update(request, pk)

    def create(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'Authentication credentials were not provided.'},
                                status=status.HTTP_401_UNAUTHORIZED)

        title = request.data.get('title')
        description = request.data.get('description')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        localisation = request.data.get('localisation')
        image = request.FILES.get('image[]')
        if not (title and description and start_time and end_time and localisation and image):
            return JsonResponse({'message': 'Please fill in all fields'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            event_service = EventService()
            event = event_service.store(request)

            notification_service = NotificationService()
            notification_service.store_event_notification()

            return JsonResponse({'message': 'Event created successfully'}, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return JsonResponse({'message': 'Validation error', 'details': e.detail},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': 'An error occurred', 'details': str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):
        title = request.data.get('title')
        description = request.data.get('description')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        localisation = request.data.get('localisation')
        image = request.FILES.get('image[]')
        if not (title and description and start_time and end_time and localisation and image):
            return JsonResponse({'message': 'Please fill in all fields'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            event_service = EventService()
            updated_event = event_service.update(pk, {
                'title': title,
                'description': description,
                'start_time': start_time,
                'end_time': end_time,
                'localisation': localisation
            }, request)
            serializer = EventSerializer(updated_event)
            return JsonResponse({'message': 'Event updated successfully', 'event': serializer.data},
                                status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return JsonResponse({'message': 'Validation error', 'details': e.detail},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': 'An error occurred', 'details': str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, action):
        if action == 'all_events':
            try:
                event_service = EventService()
                events = event_service.index(request)
                serializer = EventSerializer(events, many=True)
                return JsonResponse({'events': serializer.data}, status=status.HTTP_200_OK)
            except Exception as e:
                return JsonResponse({'message': 'An error occurred', 'details': str(e)},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete_event(self, request, pk):
        if request.method == 'DELETE':
            try:
                event_service = EventService()
                event_service.destroy(pk=pk, request=request)
                return JsonResponse({'message': 'Event deleted successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return JsonResponse({'message': 'An error occurred', 'details': str(e)},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
