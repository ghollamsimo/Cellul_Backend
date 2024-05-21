from enum import Enum

from django.db import models

from website.Models.AdminModel import Admin


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    localisation = models.CharField(max_length=200)
    def __str__(self):
        return self.title
