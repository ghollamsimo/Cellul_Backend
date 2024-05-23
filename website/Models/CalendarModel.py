from django.db import models

from website.Models.AdviseModel import Advise


class Calendar(models.Model):
    availability = models.JSONField(default=dict)
    advise = models.ForeignKey(Advise, on_delete=models.CASCADE)

    def __str__(self):
        return self.availability
