# General Imports
from django.urls import path

# Local Imports
from apps.Espn.views.authentication import login, logon, logout
from apps.Espn.views.users import get_me
urlpatterns = [
    path('login', login, name='user-login'),
    path('logon', logon, name='user-logon'),
    path('logout', logout, name='user-logout'),
    path('getMe', get_me, name='user-self-info'),
]
