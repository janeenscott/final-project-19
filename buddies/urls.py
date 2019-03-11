from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'buddies'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('users/', views.UsersInSystemView.as_view(), name='users'),
    path('user-equipment/<int:pk>/', views.UserEquipmentList.as_view(), name='user-equipment'),
]