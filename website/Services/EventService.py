from django.http import JsonResponse
from rest_framework import serializers, status
from rest_framework.decorators import api_view

from website.Models import Event
from website.Repository.Implementations.EventRepository import EventRepository
from website.Serializers.EventSerializer import EventSerializer


class EventService:
    def __init__(self):
        self.EventRepository = EventRepository()
        pass

    def all_events(self):
        return self.EventRepository.all_events()

    def store(self, request):
        return self.EventRepository.store(request)

    def update(self, pk, validated_data, request):
        try:
            updated_event = EventRepository.update(self, pk=pk, validated_data=validated_data, request=request)
            return updated_event
        except Event.DoesNotExist:
            raise serializers.ValidationError({'message': 'Event not found'})
        except Exception as e:
            raise serializers.ValidationError({'message': str(e)})

    def index(self, request):
        events = self.EventRepository.index(request)
        # print("Events:", events)
        return events

    def destroy(self, pk, request):
        event = self.EventRepository.destroy(pk=pk, request=request)
        return JsonResponse({'message': 'Event deleted successfully'})

    def show(self, pk):
        return self.EventRepository.show(pk)
