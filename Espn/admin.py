# General Imports
from django.contrib import admin

# Local Imports
from Espn import models as espn_models


@admin.register(espn_models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = [
        'user',
        'profile_picture'
    ]
    list_display = [
        'user'
    ]
    readonly_fields = [
        'access_token',
    ]
