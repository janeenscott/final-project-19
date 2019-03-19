from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.mixins import LoginRequiredMixin
from buddies.models import Message
from .serializers import MessageSerializer


class CsrfExemptMixin(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class MessageCreateView(LoginRequiredMixin, generics.ListCreateAPIView):
    # model = Message
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = (CsrfExemptMixin,)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
# sender gets automatically set to the user that is making the request (the logged in user)
#add date time_sent=self.request.something...

