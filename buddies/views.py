from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):

    template_name = 'buddies/index.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'buddies/profile.html'


# class ChatView(LoginRequiredMixin, TemplateView):
#     template_name = 'buddies/chat.html'
