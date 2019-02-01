# General Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
# Local Imports
# from  import models as espn_models
from apps.Espn import models as espn_models


class UserProfileInline(admin.StackedInline):
    model = espn_models.Profile
    fk_name = 'user'
    can_delete = False
    max_num = 1
    verbose_name_plural = 'Profile'
    fieldsets = [
        ('Profile Picture', {
            'fields': (
                'profile_picture',
                'profile_image'
            )
        }),
        ('Access Data', {
            'fields': (
                'access_token',
            )
        }

        )
    ]
    readonly_fields = [
        'access_token',
        'profile_image'
    ]


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = [
        'username',
        'email',
        'last_login',
    ]
    list_filter = [
        'last_login',
    ]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
