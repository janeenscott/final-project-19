from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.db.models import Q

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


def pair_buddies(self, request, queryset):
    for user in queryset:
        user.buddy = CustomUser.objects.exclude(
            pk=user.pk
        ).filter(
            buddy__isnull=True,
        ).filter(
            Q(rating__gt=user.rating + 5) | Q(rating__lt=user.rating - 5)
        ).order_by("?").first()

        print('user', user, 'user.buddy ', user.buddy)

        user.save()


pair_buddies.short_description = "Pair Buddies"


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', 'city', 'image', 'buddy']
    actions = [pair_buddies]


admin.site.register(CustomUser, CustomUserAdmin)
