import os
from abc import ABC

from django.shortcuts import get_object_or_404
from rest_framework import serializers, request

from core import settings
from website.Models import Event
from website.Models.UserModel import User
from website.Models.AdminModel import Admin
from website.Repository.Implementations.MediaRepository import MediaRepository
from website.Repository.Interfaces.EventInterface import EventInterface
from website.Serializers.EventSerializer import EventSerializer


class EventRepository(EventInterface, ABC):
    def store(self, data):
        user_id = data.user.id
        admin = Admin.objects.get(user_id=user_id)
        if Event.objects.filter(title=data.get('title')).exists():
            raise serializers.ValidationError({'title': 'This Event already exists'})

        try:
            event = Event.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                start_time=data.get('start_time'),
                end_time=data.get('end_time'),
                localisation=data.get('localisation'),
                admin=admin.id
            )

            return event
        except Exception as e:
            raise serializers.ValidationError({'message': 'An error occurred during event creation', 'details': str(e)})

    def update(self, pk, validated_data):
        user_id = validated_data.user.id
        admin = Admin.objects.get(user_id=user_id)
        if admin:
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
        if event is not None:
            return event
        return []

    def destroy(self, pk):
        event = get_object_or_404(Event, pk=pk)
        return event.delete()
