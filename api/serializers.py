from rest_framework.serializers import ModelSerializer

from buddies.models import Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('sender', 'message_text', 'time_sent')
        depth = 1

