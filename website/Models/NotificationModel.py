from django.db import models

from website.Models.AdviseModel import Advise
from website.Models.EventModel import Event
from website.Models.StudentModel import Student


class Notification(models.Model):
    advise_id = models.ForeignKey(Advise, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.advise_id
