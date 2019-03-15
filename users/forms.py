from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    # deleted (UserCreationForm) from after Meta. Might need that again?
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('image', 'first_name', 'city', 'age')
        # widgets = {
        #     'password': forms.PasswordInput(),
        # }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
