import os
from django.views import View
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class ChatView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(status=501)



    # def determine_if_paired(self):
    #     # user is not allowed to see page if buddy__isnull
    #     pass
