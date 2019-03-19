from rest_framework.serializers import ModelSerializer
from rest_framework.fields import JSONField

from buddies.models import Message


class MessageSerializer(ModelSerializer):
    message_text = JSONField()

    class Meta:
        model = Message
        fields = ('id', 'sender', 'message_text', 'time_sent')
        depth = 1

