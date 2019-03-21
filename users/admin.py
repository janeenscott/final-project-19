from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


def pair_buddies(self, request, queryset):
    queryset.update(buddy=fk)
    # this is not right, I need to figure out how to actually write the queryset


pair_buddies.short_description = "Pair Buddies"


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', 'city', 'image', 'buddy']
    actions = [pair_buddies]





admin.site.register(CustomUser, CustomUserAdmin)