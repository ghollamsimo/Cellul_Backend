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
            for key, value in validated_data.items():
                setattr(event, key, value)
            event.save()
            return event
        except Event.DoesNotExist:
            raise serializers.ValidationError({'message': 'Event not found'})
        except Exception as e:
            raise serializers.ValidationError({'message': str(e)})

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
