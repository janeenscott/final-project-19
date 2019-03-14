from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from .models import CustomUser
from django.views.generic import CreateView
import requests

from .forms import CustomUserCreationForm


class SignupView(CreateView):

    # **** IF USING THIS CODE, CHANGE TO CREATEVIEW *****
    model = CustomUser
    # fields = ('first_name', 'username', 'password', 'email', 'city', 'image')
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('buddies:profile')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object is the form data, queued here, but not saved
        self.object.rating = self.get_quality_rating()
        self.object.save()
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

                # self.object.rating = quality_data['teleport_city_score']

#******** UNCOMMENT ONCE MODEL IS PULLING IN FROM FOREIGN KEYS ******
    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.buddy = self.request.buddy
    #     obj.rating = self.request.rating
    #     obj.save()
    #     return HttpResponseRedirect(self.success_url())











    # WITH FORM_CLASS, SUCCESS_URL, AND TEAMPLATE_URL ONLY, DATA POSTING TO DATABASE

    #
    # def form_valid(self, form):
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password']
    #     user = authenticate(username=username, password=password)
    #     # if user is not None:
    #     #     if user.is_active:
    #     #         login(request, user)
    #     #         reverse_lazy(success_url)
    #     return HttpResponseRedirect(reverse('buddies:index'))

    # ******** IF USING THIS CODE, CHANGE TO TEMPLATEVIEW *****
    # template_name = 'users/signup.html'
    #
    # def post(self, request, *args, **kwargs):
    #
    #     #sign up user
    #
    #     first_name = self.request.POST.get('first_name')
    #
    #     username = self.request.POST.get('username')
    #     password = self.request.POST.get('password')
    #     password2 = self.request.POST.get('password2')
    #
    #     email = self.request.POST.get('email')
    #     phone_number = self.request.POST.get('phone_number')
    #     zipcode = self.request.POST.get('zipcode')
    #     city = self.request.POST.get('city')
    #     state = self.request.POST.get('state')
    #     age = self.request.POST.get('age')
    #     image = self.request.POST.get('image')
    #
    #     print(self.request)
    #
    #     if password != password2:
    #         return HttpResponseRedirect(reverse('users:signup'))
    #     if password != password2:
    #         return HttpResponseRedirect(reverse('users:signup'))
    #
    #     # If the username already exists, send the user back
    #     user = CustomUser.objects.filter(username=username)
    #     if user.count() > 0:
    #         return HttpResponseRedirect(reverse('users:signup'))
    #
    #     # save user database record using fancy hashing on password
    #     CustomUser.objects.create_user(first_name=first_name, username=username, password=password, email=email, phone_number=phone_number, zipcode=zipcode, city=city, state=state, age=age, image=image)
    #
    #     # Authenticate the user checks provided password against the hash
    #     user = authenticate(username=username, password=password)
    #
    #     # Login the user (does the session table/cookie stuff)
    #     login(self.request, user)
    #
        # return HttpResponseRedirect(reverse('buddies:index'))


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


