from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from .models import CustomUser
from django.views.generic import CreateView, UpdateView
import requests

from .forms import CustomUserCreationForm


class SignupView(CreateView):

    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('buddies:profile')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object is the form data, queued here, but not saved
        self.object.rating = self.get_quality_rating()
        self.object.save()
        login(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())

    def get_quality_rating(self):

        city_stat_url = 'https://api.teleport.org/api/urban_areas/slug:{}/scores/'.format(self.object.city.lower())
        response = requests.get(city_stat_url)
        quality_data = response.json()

        print(quality_data)

        score = quality_data['teleport_city_score']

        # print('quality data: ', quality_data)
        print('score: ', score)

        return score


# class UpdateProfileView(UpdateView):
#
#     model = CustomUser
#     form_class = CustomUserCreationForm
#     context_object_name = 'profile'
#     # queryset =
#
#     # def form_valid(self, form):
#     #     profile = form.save(commit=False)
#     #     profile.updated_by = self.request.user
#     #     profile.save()
#     #     return redirect('buddies:profile')


class LoginView(TemplateView):
    template_name = 'users/login.html'

    def login_user(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return HttpResponseRedirect(reverse('buddies:profile'))


