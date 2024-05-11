from django.db import models

from website.Models.AdviseModel import Advise
from website.Models.StudentModel import Student


class NotificationModel(models.Model):
    advise_id = models.ForeignKey(Advise, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.advise_id
