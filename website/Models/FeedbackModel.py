from enum import Enum

from django.db import models

from website.Models.StudentModel import Student


class Status(Enum):
    Waiting = 'Waiting'
    Accepted = "Accepted"
    Rejected = "Rejected"

    @classmethod
    def choices(cls):
        return [(role.value, role.name) for role in cls]


class Feedback(models.Model):
    feedback = models.TextField(max_length=255)
    advise = models.ForeignKey('Advise', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=Status.choices(), default=Status.Waiting.value)

    def __str__(self):
        return self.student
