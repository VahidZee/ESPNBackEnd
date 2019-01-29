# General Imports
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import secrets as python_secrets

import json

# Model Imports
from apps.Espn import models as espn_models



def create_new_access_token(profile: espn_models.Profile) -> str:
    profile.token = python_secrets.token_urlsafe(nbytes=256)
    profile.save()
    return profile.token


def user_password_was_incorrect() -> JsonResponse:
    return JsonResponse(data={
        'ok': False,
        'description': "Password was Incorrect",
    })


def token_was_not_found() -> JsonResponse:
    return JsonResponse(data={
        'ok': False,
        'description': "Incorrect Access Token",
    })


def user_profile_not_found() -> JsonResponse:
    return JsonResponse(data={
        'ok': False,
        'description': "User Profile Was Not Found",
    })


def api_method_not_found() -> JsonResponse:
    return JsonResponse(data={
        'ok': False,
        'description': "Method Not Found - For Security Reasons API Methods are only available through POST method",
    })


def get_profile(token) -> espn_models.Profile:
    try:
        profile = espn_models.Profile.objects.get(access_token__exact=token)
    except Exception:
        raise Exception
    return profile


def find_profile_decorator(funct: callable):
    @method_decorator(csrf_exempt, name='dispatch')
    def wrapper(request):
        try:
            data = json.loads(request.body)
            profile = get_profile(data['token'])
            return funct(request, profile)
        except Exception:
            return user_profile_not_found()
    return wrapper
