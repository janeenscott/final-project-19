import os
from django.views import View
from django.http import HttpResponse
from django.conf import settings


class ChatView(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(status=501)


