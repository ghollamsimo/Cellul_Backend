from django.db import models

from website.Models.EventModel import Event


class Media(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.event_id
