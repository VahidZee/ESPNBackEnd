from django.http import JsonResponse
from apps.Espn import models as espn_models
import secrets as python_secrets


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
        profile = espn_models.Profile.objects.get(token__exact=token)
    except Exception:
        raise Exception
    return profile



