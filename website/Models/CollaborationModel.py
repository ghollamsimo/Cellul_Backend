from django.db import models

from website.Models.AdminModel import Admin


class Collaboration(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
