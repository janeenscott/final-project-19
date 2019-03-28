from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'buddies'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('about/', views.AboutView.as_view(), name='about'),

    # path('chat/', views.ChatView.as_view(), name='chat'),
]
