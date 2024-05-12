from django.db import models

from website.Models.AdviseModel import Advise


class Calendar(models.Model):
    time = models.DateTimeField(auto_now_add=False)
    date = models.DateField(auto_now=False)
    advise_id = models.ForeignKey(Advise, on_delete=models.CASCADE)

    def __str__(self):
        return self.time
