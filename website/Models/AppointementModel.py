from enum import Enum
from django.db import models


class Status(Enum):
    Waiting = 'Waiting'
    Accepted = "Accepted"
    Rejected = "Rejected"

    @classmethod
    def choices(cls):
        return [(role.value, role.name) for role in cls]


class Appointment(models.Model):
    advise = models.ForeignKey('Advise', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    status = models.CharField(max_length=255, choices=Status.choices(), default=Status.Waiting.value)
    time = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.advise)
