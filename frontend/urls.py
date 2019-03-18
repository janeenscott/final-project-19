"""
users app urls
"""

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'frontend'

urlpatterns = [
    path('chat/', views.ChatView.as_view(), name='chat'),
]