from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view

from website.Services.EventService import EventService


@api_view(['POST'])
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        localisation = request.POST.get('localisation')

        if not localisation or not title or not start_time or not end_time or not description:
            return JsonResponse({'message': 'Please Fill in fields'})

        try:
            event_service = EventService()
            event = event_service.store(
                {'title': title, 'description': description, 'start_time': start_time, 'end_time': end_time,
                 'localisation': localisation}
            )
            return JsonResponse({'metadata': 'Event Created Successfully'})
        except serializers.ValidationError as e:
            return JsonResponse({'message': 'Validation error', 'details': e.detail}, status=400)


@api_view(['PUT'])
def update_event(request, pk):
    title = request.POST.get('title')
    description = request.POST.get('description')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    localisation = request.POST.get('localisation')

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
        return JsonResponse({'message': 'Event updated successfully', 'event': updated_event}, status=200)
    except serializers.ValidationError as e:
        return JsonResponse({'message': 'Validation error', 'details': e.detail}, status=400)
    except Exception as e:
        return JsonResponse({'message': 'An error occurred', 'details': str(e)}, status=500)


@api_view(['GET'])
def all_event(request):
    if request.method == 'GET':
        event_service = EventService()
        response = event_service.index(request)
        print("Response:", response)
        return response


@api_view(['DELETE'])
def delete_event(request, pk):
    if request.method == 'DELETE':
        event_service = EventService()
        event = event_service.destroy(pk=pk)
        return event
