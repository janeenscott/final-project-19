from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = 'buddies/index.html'


class ProfileView(TemplateView):
    template_name = 'buddies/profile.html'


class ChatView(TemplateView):
    template_name = 'buddies/chat.html'
