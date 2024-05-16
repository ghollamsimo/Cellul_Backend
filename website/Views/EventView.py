from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view

from website.Services.EventService import EventService
from website.Services.NotificationService import NotificationService
from website.Serializers.EventSerializer import EventSerializer


@api_view(['POST'])
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        localisation = request.POST.get('localisation')

        if not localisation or not title or not start_time or not end_time or not description:
            return JsonResponse({'message': 'Please fill in all fields'}, status=400)

        try:
            event_service = EventService()
            event = event_service.store(
                {'title': title, 'description': description, 'start_time': start_time, 'end_time': end_time,
                 'localisation': localisation}
            )
            notification_service = NotificationService()
            notification = notification_service.store_event_notification()

            return JsonResponse({'message': 'Event created successfully'})
        except serializers.ValidationError as e:
            return JsonResponse({'message': 'Validation error', 'details': e.detail}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@api_view(['PUT'])
def update_event(request, pk):
    title = request.data.get('title')
    description = request.data.get('description')
    start_time = request.data.get('start_time')
    end_time = request.data.get('end_time')
    localisation = request.data.get('localisation')

    if not (title and description and start_time and end_time and localisation):
        return JsonResponse({'message': 'Please fill in all fields'}, status=400)

    try:
        event_service = EventService()
        updated_event = event_service.update(
            pk,
            {
                'title': title,
                'description': description,
                'start_time': start_time,
                'end_time': end_time,
                'localisation': localisation
            }
        )
        serializer = EventSerializer(updated_event)
        return JsonResponse({'message': 'Event updated successfully', 'event': serializer.data}, status=200)
    except serializers.ValidationError as e:
        return JsonResponse({'message': 'Validation error', 'details': e.detail}, status=400)
    except Exception as e:
        return JsonResponse({'message': 'An error occurred', 'details': str(e)}, status=500)
@api_view(['GET'])
def all_event(request):
    if request.method == 'GET':
        event_service = EventService()
        response = event_service.index(request)
        events = EventSerializer(response, many=True).data
        print("Response:", events)
        return JsonResponse({'events': events}, status=200)


@api_view(['DELETE'])
def delete_event(request, pk):
    if request.method == 'DELETE':
        event_service = EventService()
        event = event_service.destroy(pk=pk)
        return event
