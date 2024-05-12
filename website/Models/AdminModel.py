from website.Models.UserModel import User
from django.db import models


class Admin(models.Model):
    class Meta:
        app_label = 'website'

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
