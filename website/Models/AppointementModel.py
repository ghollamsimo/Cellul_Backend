from django.db import models

from website.Models import Advise, Student


class Appointment(models.Model):
    advise = models.ForeignKey(Advise, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    time = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.advise