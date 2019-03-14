from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from phone_field import PhoneField
from localflavor.us.models import USStateField


class CustomUser(AbstractUser):
    CITY_CHOICES = (
        ('albuquerque', 'ALBUQUERQUE'),
        ('anchorage', 'ANCHORAGE'),
        ('asheville', 'ASHEVILLE'),
        ('atlanta', 'ATLANTA'),
        ('austin', 'AUSTIN'),
        ('baltimore', 'BALTIMORE'),
        ('birmingham_al', 'BIRMINGHAM_AL'),
        ('boise', 'BOISE')
    )

    first_name = models.CharField(max_length=50, null=True)
    # password = models.CharField(max_length=15, widget=forms.PasswordInput)
    # last_name = models.CharField(max_length=50, null=True)
    # username = models.CharField(max_length=50, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        # unique=True,
        null=True
    )
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    zipcode = models.IntegerField(null=True)
    city = models.CharField(max_length=100, choices=CITY_CHOICES, default='ALBUQUERQUE', null=True)
    state = USStateField(null=True)
    age = models.CharField(max_length=2, null=True)
    image = models.ImageField(null=True, upload_to='media/', default='static/images/placeholder.jpg')
    buddy = models.ForeignKey('users.CustomUser', null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(decimal_places=5, max_digits=7)

    def __str__(self):
        return self.username


