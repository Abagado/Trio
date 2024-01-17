from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.contrib.auth.models import Permission
from django.conf import settings


class CustomUser(AbstractUser):
    score = models.IntegerField(default=0)

    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


class UserRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.score} points"
