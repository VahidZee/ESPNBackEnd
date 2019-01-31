# General Imports
from django.urls import path

# Local Imports
from apps.Espn.views.authentication import login, logon, \
    logout, forgot_password, reset_password, \
    activate_account
from apps.Espn.views.users import get_me

urlpatterns = [
    path('login', login, name='user-login'),
    path('logon', logon, name='user-logon'),
    path('logout', logout, name='user-logout'),
    path('getMe', get_me, name='user-self-info'),
    path('forgot_password', forgot_password, name='user-forgot-passoword'),
    path('reset_password', reset_password, name='user-reset-password'),
    path('activate_account', activate_account, name='user-account-activation')
]
