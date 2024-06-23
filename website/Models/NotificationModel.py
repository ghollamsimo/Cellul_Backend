from django.db import models

from website.Models.AppointementModel import Appointment
from website.Models.AdviseModel import Advise
from website.Models.EventModel import Event
from website.Models.StudentModel import Student


class Notification(models.Model):
    advise = models.ForeignKey(Advise, null=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
