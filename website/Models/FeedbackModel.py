from django.db import models

from website.Models.StudentModel import Student


class Feedback(models.Model):
    feedback = models.TextField(max_length=255)
    shared = models.BooleanField(default=False)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id
