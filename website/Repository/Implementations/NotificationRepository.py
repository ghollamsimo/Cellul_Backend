from abc import ABC

from website.Models.EventModel import Event
from website.Models.StudentModel import Student
from website.Models.NotificationModel import Notification
from website.Repository.Interfaces.NotificationInterface import NotificationInterface


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
