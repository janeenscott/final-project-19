from django.urls import path
from rest_framework import routers

from . import views

app_name = 'api'

urlpatterns = [
    path('api/message/', views.MessageCreateView.as_view()),
]
