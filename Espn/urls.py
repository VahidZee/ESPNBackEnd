# General Imports
from django.urls import path

# Local Imports
from Espn import views as espn_views

urlpatterns = [
    path('login', espn_views.login, name="user-login")
]
