from django.shortcuts import render
from rest_framework import viewsets, generics
from buddies.models import Message
from .serializers import MessageSerializer


class MessageCreateView(generics.ListCreateAPIView):
    # model = Message
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
