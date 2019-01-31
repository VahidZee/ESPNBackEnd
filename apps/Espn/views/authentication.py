# General Imports
from django.http import JsonResponse

from django.contrib.auth.hashers import make_password

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.core.validators import validate_email

from datetime import datetime

import json

# Models Imports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from apps.Espn import models as espn_models

# Local Imports
from apps.Espn import methods as espn_methods
from apps.Espn.methods import find_profile_decorator


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
def logout(request, profile) -> JsonResponse:
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
            if data['username'] == '':
                return JsonResponse(
                    data={
                        'ok': False,
                        'description': 'Username name shouldn\'t be blank'
                    }
                )
            user.username = data['username']
            if data['password'] == '':
                return JsonResponse(
                    data={
                        'ok': False,
                        'description': 'password shouldn\'t be blank'
                    }
                )
            user.password = make_password(data['password'])
            if data['email'] == '':
                return JsonResponse(
                    data={
                        'ok': False,
                        'description': 'email shouldn\'t be blank'
                    }
                )
            try:
                validate_email(data['email'])
            except Exception:
                return JsonResponse(
                    data={
                        'ok': False,
                        'description': 'Please enter a valid Email'
                    }
                )
            user.email = data['email']
            if data['first_name'] == '':
                return JsonResponse(
                    data={
                        'ok': False,
                        'description': 'First name shouldn\'t be blank'
                    }
                )
            user.first_name = data['first_name']
            if data['last_name'] == '':
                return JsonResponse(
                    data={
                        'ok': False,
                        'description': 'Last name shouldn\'t be blank'
                    }
                )
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


@method_decorator(csrf_exempt, name='dispatch')
def forget_password(request):
    try:
        data = json.loads(request.body)
        
    except Exception:
        return JsonResponse(
            data={
                'ok': True,
                'description': 'Unknown Error Occured'
            }
        )