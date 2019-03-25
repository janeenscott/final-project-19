from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.mixins import LoginRequiredMixin
from buddies.models import Message
from .serializers import MessageSerializer
from django.db.models import Q


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

    def get_queryset(self):
        queryset = Message.objects.filter(
                Q(sender=self.request.user) | Q(sender=self.request.user.buddy)
            ).order_by('time_sent')
        return queryset


class MessageUpdateView(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = (CsrfExemptMixin,)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        queryset = Message.objects.filter(
            Q(sender=self.request.user) | Q(sender=self.request.user.buddy)
        ).order_by('time_sent')
        return queryset

    # def get_object(self):
    #     object.queryset = Message.objects.filter(user=self.request.user)
    #     can_edit = Message.objects.get(pk=pk).first()
    #     return can_edit
    # this is working kind of.... allows both users to go to edit screen, but does not save
    # edits.... unfortunately that is also for both users

    # return self.Message.objects.get(pk=self.request.user.pk)


class MessageDeleteView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = (CsrfExemptMixin,)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        queryset = Message.objects.filter(
            Q(sender=self.request.user) | Q(sender=self.request.user.buddy)
        ).order_by('time_sent')
        return queryset
