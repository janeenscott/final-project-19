from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model, login, authenticate
from .models import CustomUser
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignupView(TemplateView):
    # form_class = CustomUserCreationForm
    # success_url = reverse_lazy('login')
    # template_name = 'users/signup.html'

    template_name = 'users/signup.html'

    def post(self, request, *args, **kwargs):

        #sign up user

        first_name = self.request.POST.get('first_name')

        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        password2 = self.request.POST.get('password2')

        if password != password2:
            return HttpResponseRedirect(reverse('users:signup'))
        if password != password2:
            return HttpResponseRedirect(reverse('users:signup'))

        # If the username already exists, send the user back
        user = CustomUser.objects.filter(username=username)
        if user.count() > 0:
            return HttpResponseRedirect(reverse('users:signup'))

        # save user database record using fancy hashing on password
        CustomUser.objects.create_user(username=username, password=password)

        # Authenticate the user checks provided password against the hash
        user = authenticate(username=username, password=password)

        # Login the user (does the session table/cookie stuff)
        login(self.request, user)

        return HttpResponseRedirect(reverse('buddies:index'))


class LoginView(TemplateView):
    template_name = 'users/login.html'

    def login_user(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return HttpResponseRedirect(reverse('users:index'))


