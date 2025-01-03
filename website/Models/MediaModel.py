from django.db import models

from website.Models.EventModel import Event


class Media(models.Model):
    image_path = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_path
