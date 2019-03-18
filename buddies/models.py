from django.db import models
from django.utils import timezone


from users.models import CustomUser


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    message_text = models.TextField(default='')
    time_sent = models.DateTimeField(default=timezone.now)
