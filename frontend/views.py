import os
from django.views import View
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class ChatView(LoginRequiredMixin, View):
    def get(self, request):
        print('chat')
        user = self.request.user
        print(user)

        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:

                html = f.read()
                html = html.replace('{{ request.user.pk }}', str(user.pk))

                return HttpResponse(html)

        except FileNotFoundError:
            return HttpResponse(status=501)



    # def determine_if_paired(self):
    #     # user is not allowed to see page if buddy__isnull
    #     pass
