from abc import ABC

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from website.Models import Event
from website.Repository.Interfaces.EventInterface import EventInterface
from website.Serializers.EventSerializer import EventSerializer


class EventRepository(EventInterface, ABC):
    def store(self, validated_data):
        title = validated_data.pop('title')
        description = validated_data.pop('description')
        start_time = validated_data.pop('start_time')
        end_time = validated_data.pop('end_time')
        localisation = validated_data.pop('localisation')

        if Event.objects.filter(title=title).exists():
            raise serializers.ValidationError({'title': 'This Event already exists'})

        event = Event.objects.update_or_create(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            localisation=localisation
        )

        return event

    def update(self, pk, validated_data):
        try:
            event = Event.objects.get(pk=pk)
            event_serializer = EventSerializer(instance=event, data=validated_data)
            if event_serializer.is_valid():
                event_serializer.save()
                return event_serializer
            else:
                raise serializers.ValidationError(event_serializer.errors)
        except Event.DoesNotExist:
            raise serializers.ValidationError({'message': 'Event not found'})

        pass

    def index(self, request):
        if request.query_params:
            event = Event.objects.filter(**request.query_params.dict())
        else:
            event = Event.objects.all()
        print("Queryset:", event)
        if event is not None:
            return event
        return []

    def destroy(self, pk):
        event = get_object_or_404(Event, pk=pk)
        return event.delete()
