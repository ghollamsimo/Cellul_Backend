from enum import Enum
from django.db import models


class Role(Enum):
    Admin = "Admin"
    Student = "Student"
    Advise = 'Advise'

    @classmethod
    def choices(cls):
        return [(role.value, role.name) for role in cls]


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=255, choice=Role.choices())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
