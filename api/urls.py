from django.urls import path
from rest_framework import routers

from . import views

app_name = 'api'

urlpatterns = [
    path('api/message/', views.MessageCreateView.as_view()),
    path('api/message/<int:pk>/', views.MessageUpdateView.as_view()),
    path('api/message/delete/<int:pk>/', views.MessageDeleteView.as_view()),
]
