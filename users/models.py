from django.contrib.auth.models import AbstractUser
from django.db import models
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
    # last_name = models.CharField(max_length=50, null=True)
    # username = models.CharField(max_length=50, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    zipcode = models.IntegerField(null=True)
    city = models.CharField(max_length=100, choices=CITY_CHOICES, default='ALBUQUERQUE', null=True)
    state = USStateField(null=True)
    age = models.CharField(max_length=2, null=True)
    image = models.ImageField(null=True, upload_to='media/', default='static/images/placeholder.jpg')

    def __str__(self):
        return self.username


