from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from .models import CustomUser
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignupView(CreateView):

    # **** IF USING THIS CODE, CHANGE TO CREATEVIEW *****
    # model = CustomUser
    # fields = ('first_name', 'username', 'password', 'email', 'city', 'image')
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('buddies:profile')
    template_name = 'users/signup.html'

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
    #     return HttpResponseRedirect(reverse('buddies:index'))


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


