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
        ('Birmingham, AL', 'Birmingham, AL'),
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
        ('Colorado Springs', 'Colorado Springs'),
        ('Columbus', 'Columbus'),
        ('Dallas', 'Dallas'),
        ('Denver', 'Denver'),
        ('Des Moines', 'Des Moines'),
        ('Detroit', 'Detroit'),
        ('Eugene', 'Eugene'),
        ('Fort Collins', 'Fort Collins'),
        ('Honolulu', 'Honolulu'),
        ('Houston', 'Houston'),
        ('Indianapolis', 'Indianapolis'),
        ('Jacksonville', 'Jacksonville'),
        ('Kansas City', 'Kansas City'),
        ('Knoxville', 'Knoxville'),
        ('Las Vegas', 'Las Vegas'),
        ('Los Angeles', 'Los Angeles'),
        ('Louisville', 'Louisville'),
        ('Madison', 'Madison'),
        ('Memphis', 'Memphis'),
        ('Miami', 'Miami'),
        ('Milwaukee', 'Milwaukee'),
        ('Minneapolis-Saint Paul', 'Minneapolis-Saint Paul'),
        ('Nashville', 'Nashville'),
        ('New Orleans', 'New Orleans'),
        ('New York', 'New York'),
        ('Oklahoma City', 'Oklahoma City'),
        ('Omaha', 'Omaha'),
        ('Orlando', 'Orlando'),
        ('Palo Alto', 'Palo Alto'),
        ('Philadelphia', 'Philadelphia'),
        ('Phoenix', 'Phoenix'),
        ('Pittsburgh', 'Pittsburgh'),
        ('Portland, ME', 'Portland, ME'),
        ('Portland, OR', 'Portland, OR'),
        ('Providence', 'Providence'),
        ('Raleigh', 'Raleigh'),
        ('Richmond', 'Richmond'),
        ('Rochester', 'Rochester'),
        ('Salt Lake City', 'Salt Lake City'),
        ('San Antonio', 'San Antonio'),
        ('San Diego', 'San Diego'),
        ('San Francisco Bay Area', 'San Francisco Bay Area'),
        ('Seattle', 'Seatte'),
        ('St. Louis', 'St. Louis'),
        ('Tampa Bay Area', 'Tampa Bay Area'),
        ('Washington, D.C.', 'Washington, D.C.')
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


