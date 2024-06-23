import os
from abc import ABC

from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404
from rest_framework import serializers, request
from django.core.exceptions import ValidationError

from core import settings
from website.Models import Event, Media
from website.Models.UserModel import User
from website.Models.AdminModel import Admin
from website.Repository.Implementations.MediaRepository import MediaRepository
from website.Repository.Interfaces.EventInterface import EventInterface
from website.Serializers.EventSerializer import EventSerializer


class EventRepository(EventInterface, ABC):
    def all_events(self):
        events = Event.objects.all()
        return events
        pass

    def store(self, request):
        if not request.user.is_authenticated:
            raise serializers.ValidationError({'detail': 'Authentication credentials were not provided.'})

        user_id = request.user.id
        admin = get_object_or_404(Admin, user_id=user_id)

        title = request.data.get('title')
        if Event.objects.filter(title=title).exists():
            raise serializers.ValidationError({'title': 'This Event already exists'})

        try:
            event = Event(
                title=title,
                description=request.data.get('description'),
                start_time=request.data.get('start_time'),
                end_time=request.data.get('end_time'),
                localisation=request.data.get('localisation'),
                admin=admin
            )
            event.full_clean()
            event.save()

            images = request.FILES.getlist('image[]')
            for image in images:
                file_path = default_storage.save(os.path.join('media', image.name), image)
                file_path = 'http://192.168.1.105:8000/' + file_path
                Media.objects.create(event=event, image_path=file_path)

            return event
        except ValidationError as e:
            raise serializers.ValidationError({'message': 'Validation error', 'details': e.message_dict})
        except Exception as e:
            raise serializers.ValidationError({'message': 'An error occurred during event creation', 'details': str(e)})

    def update(self, pk, validated_data, request):
        try:
            user_id = request.user.id
            admin = Admin.objects.get(user_id=user_id)
            if not admin:
                raise serializers.ValidationError({'detail': 'User is not authorized to perform this action'})

            event = Event.objects.get(pk=pk, admin=admin)

            for key, value in validated_data.items():
                setattr(event, key, value)
            event.save()
            event.media_set.all().delete()

            if 'images' in request.FILES:
                images = request.FILES.getlist('image[]')
                for image in images:
                    file_path = default_storage.save(os.path.join('media', image.name), image)
                    media = Media.objects.create(event=event, image_path=file_path)

            return event
        except Event.DoesNotExist:
            raise serializers.ValidationError({'message': 'Event not found'})
        except Admin.DoesNotExist:
            raise serializers.ValidationError({'message': 'Admin not found'})
        except ValidationError as e:
            raise serializers.ValidationError({'message': 'Validation error', 'details': e.message_dict})
        except Exception as e:
            raise serializers.ValidationError({'message': 'An error occurred during event update', 'details': str(e)})

    def index(self, request):
        user_id = request.user.id
        admin = Admin.objects.get(user_id=user_id)
        if admin:
            if request.query_params:
                event = Event.objects.prefetch_related('media_set').filter(**request.query_params.dict(),
                                                                           admin_id=admin)
            else:
                event = Event.objects.all()
            if event is not None:
                return event
            return []

    def destroy(self, pk, request):
        user_id = request.user.id
        admin = Admin.objects.get(user_id=user_id)
        if admin:
            event = get_object_or_404(Event, pk=pk)
            return event.delete()


    def show(self, pk):
        event = get_object_or_404(Event, id=pk)
        return event
        pass