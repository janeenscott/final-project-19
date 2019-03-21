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
        # response = requests.get('https://api.teleport.org/api/urban_areas/')
        # urban_areas = response.json()
        # # print(urban_areas)
        # city_list = urban_areas['_links']["ua:item"]
        # user_city = ''
        #
        #
        # for city in city_list:
        #     if city['name'] == self.object.city:
        #         # while iterating over all cities in API,
        #         # if the specific city name in the ua:item dictionary
        #         # matches the city that the user selected...
        #         # print('username and city: ', self.object.username, self.object.city)
        #         user_city = city['href']
        # print('user city: ', user_city)
        # # print('user city href: ', user_city_href)
        city_stat_url = 'https://api.teleport.org/api/urban_areas/slug:{}/scores/'.format(self.object.city.lower())
        response = requests.get(city_stat_url)
        quality_data = response.json()

        print(quality_data)

        score = quality_data['teleport_city_score']

        # print('quality data: ', quality_data)
        print('score: ', score)

        return score

#******** UNCOMMENT ONCE MODEL IS PULLING IN FROM FOREIGN KEYS ******
    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.buddy = self.request.buddy
    #     obj.rating = self.request.rating
    #     obj.save()
    #     return HttpResponseRedirect(self.success_url())


# class UpdtateProfileView(UpdateView):
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


