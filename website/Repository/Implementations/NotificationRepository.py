from abc import ABC

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from website.Models.AppointementModel import Appointment
from website.Models.EventModel import Event
from website.Models.StudentModel import Student
from website.Models.NotificationModel import Notification
from website.Repository.Interfaces.NotificationInterface import NotificationInterface
from website.Models.AdviseModel import Advise


class NotificationRepository(NotificationInterface, ABC):

    def store_of_event(self):
        students = Student.objects.all()
        event = Event.objects.latest('id')

        notifications = []
        for student in students:
            notification = Notification.objects.create(
                advise=None,
                student=student,
                event=event,
                appointment=None,
                message='New Event Has Been Created: ' + event.title
            )
            notifications.append(notification)

        return notifications
        pass

    def store_of_appointment(self):
        students = Student.objects.all()
        advise = Advise.objects.all()
        appointment = Appointment.objects.latest('id')
        notifications = []
        if students:
            for student in students:
                notification = Notification.objects.create(
                    advise=advise,
                    student=student,
                    event=None,
                    message='New Appointment Has Been Added',
                    appointment=appointment
                )
                notifications.append(notification)
            return notifications
        else:
            return serializers.ValidationError({'message': 'Student Not Found'})
        pass

    def destroy_of_event(self, request, pk):
        user_id = request.data.get('user_id')
        student = Student.objects.get(user_id=user_id)
        if student:
            notification = get_object_or_404(Notification, pk=pk)
            return notification.delete()
        else:
            return serializers.ValidationError({"message": 'Student not found'})
        pass

    def destroy_of_appointment(self, request, pk):
        user_id = request.user.id
        advise = Advise.objects.get(user_id=user_id)
        if advise:
            notification = get_object_or_404(Notification, pk=pk)
            return notification.delete()
        else:
            return serializers.ValidationError({"message": 'Student not found'})
        pass