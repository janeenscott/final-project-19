from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from phone_field import PhoneField
from localflavor.us.models import USStateField


class CustomUser(AbstractUser):
    CITY_CHOICES = (
        ('Albuquerque', 'Albuquerque'),
        ('Anchorage', 'Anchorage'),
        ('Asheville', 'Asheville'),
        ('Atlanta', 'Atlanta'),
        ('Austin', 'Austin'),
        ('Baltimore', 'Baltimore'),
        ('Boise', 'Boise'),
        ('Boston', 'Boston'),
        ('Boulder', 'Boulder'),
        ('Buffalo', 'Buffalo'),
        ('Charleston', 'Charleston'),
        ('Charlotte', 'Charlotte'),
        ('Chattanooga', 'Chattanooga'),
        ('Chicago', 'Chicago'),
        ('Cincinnati', 'Cincinnati'),
        ('Cleveland', 'Cleveland'),
        ('Columbus', 'Columbus'),
        ('Dallas', 'Dallas'),
        ('Denver', 'Denver'),
        ('Detroit', 'Detroit'),
        ('Eugene', 'Eugene'),
        ('Honolulu', 'Honolulu'),
        ('Houston', 'Houston'),
        ('Indianapolis', 'Indianapolis'),
        ('Jacksonville', 'Jacksonville'),
        ('Kansas City', 'Kansas City'),
        ('Knoxville', 'Knoxville'),
        ('Louisville', 'Louisville'),
        ('Madison', 'Madison'),
        ('Memphis', 'Memphis'),
        ('Miami', 'Miami'),
        ('Milwaukee', 'Milwaukee'),
        ('Nashville', 'Nashville'),
        ('Omaha', 'Omaha'),
        ('Orlando', 'Orlando'),
        ('Philadelphia', 'Philadelphia'),
        ('Phoenix', 'Phoenix'),
        ('Pittsburgh', 'Pittsburgh'),
        ('Providence', 'Providence'),
        ('Raleigh', 'Raleigh'),
        ('Richmond', 'Richmond'),
        ('Rochester', 'Rochester'),
        ('Seattle', 'Seatte'),
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
    age = models.IntegerField(null=True)
    image = models.ImageField(null=True, upload_to='media/', default='static/images/placeholder.jpg')
    # maybe change buddy to a OnetoOne field to correct for duplicates
    buddy = models.ForeignKey('users.CustomUser', null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(decimal_places=5, max_digits=7)

    def __str__(self):
        return self.username


