# General Imports
from django.http import JsonResponse

from django.contrib.auth.hashers import make_password

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from apps.Espn.methods import find_profile_decorator
from datetime import datetime

import json

# Models Imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from apps.Espn import models as espn_models

# Local Imports
from apps.Espn import methods as espn_methods


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
def login(request) -> JsonResponse:
    try:
        data = json.loads(request.body)
        user = authenticate(request, username=data['username'], password=data['password'])
        profile = espn_models.Profile.objects.get(user=user)
    except Exception:
        return espn_methods.user_profile_not_found()
    token = espn_methods.create_new_access_token(profile)
    profile.user.last_login = datetime.now()
    profile.user.save()
    profile.access_token = token
    profile.save()
    return JsonResponse(data={
        'ok': True,
        'token': token
    })


@find_profile_decorator
def logout(request,profile) -> JsonResponse:
    profile.access_token = ''
    profile.save()
    return JsonResponse(
        data={
            'ok': True,
            'description': 'Logged out successfully'
        }
    )


@method_decorator(csrf_exempt, name='dispatch')
def logon(request):
    try:
        data = json.loads(request.body)
        if User.objects.all().filter(username__exact=data['username']).count() == 0:
            user = User()
            user.username = data['username']
            user.password = make_password(data['password'])
            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            profile = espn_models.Profile(user=user)
            profile.save()
        else:
            return JsonResponse(
                data={
                    'ok': False,
                    'description': 'Username is already taken'
                }
            )
    except Exception:
        return JsonResponse(
            data={
                'ok': False,
                'description': 'Logon Data was incorrect'
            }
        )
    token = espn_methods.create_new_access_token(profile)
    return JsonResponse(
        data={
            'ok': True,
            'description': 'Logged On successfully'
        }
    )
