from django.urls import path
from rest_framework import routers

from . import views

app_name = 'api'

urlpatterns = [
    path('api/message/', views.MessageCreateView.as_view(
    #     {
    #     'get': 'list',  # GET method should list objects
    #     'post': 'create',  # POST method should create object
    # }
    )),
]
