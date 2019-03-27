from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.db.models import Q

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


def pair_buddies(self, request, queryset):
    for user in queryset:

        user.refresh_from_db()
        if user.buddy is not None:
            continue

        buddy = CustomUser.objects.exclude(
            pk=user.pk
        ).filter(
            pk__in=[selected.pk for selected in queryset],
            buddy__isnull=True
        ).filter(
            Q(rating__gt=user.rating + 5) | Q(rating__lt=user.rating - 5)
        ).filter(
            Q(age__gt=int(user.age) - 2) & Q(age__lt=int(user.age) + 2)
        ).order_by("?").first()

        if buddy is None:
            continue

        user.buddy = buddy
        buddy.buddy = user

        # print('user', user, 'user.buddy ', user.buddy)

        user.save()
        buddy.save()


pair_buddies.short_description = "Pair Buddies"


def clear_buddies(self, request, queryset):
    queryset.update(buddy=None)
    # for user in queryset:
    #     user.buddy = CustomUser.objects.update(buddy='null')


clear_buddies.short_description = 'Clear Buddies'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', 'city', 'rating', 'buddy']
    actions = [pair_buddies, clear_buddies]


admin.site.register(CustomUser, CustomUserAdmin)
