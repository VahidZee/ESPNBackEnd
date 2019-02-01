# General Imports
from django.core.mail import send_mail
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import secrets as python_secrets

import json

# Model Imports
from apps.Espn import models as espn_models


def create_new_access_token(profile: espn_models.Profile) -> str:
    profile.access_token = python_secrets.token_urlsafe(nbytes=256)
    profile.save()
    return profile.access_token


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
            if not profile.active:
                raise Exception
            return funct(request, profile)
        except Exception:
            return user_profile_not_found()

    return wrapper


def find_profile_if_exists_decorator(funct: callable):
    @method_decorator(csrf_exempt, name='dispatch')
    def wrapper(request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            profile = get_profile(data['token'])
            if not profile.active:
                raise Exception
            return funct(request, *args, profile=profile, logged_in=True, **kwargs)
        except Exception:
            return funct(request, *args, profile=None, logged_in=False, **kwargs)

    return wrapper


def create_forget_password_token(email: str):
    try:
        profile = espn_models.Profile.objects.get(user__email=email)
        profile.forget_password_access_token = python_secrets.token_urlsafe(nbytes=256)
        profile.save()
    except Exception:
        return False, None
    return profile.forget_password_access_token, profile


def send_forget_password_email(profile: espn_models.Profile, token: str):
    subject = 'Your Forget Password Token'
    body = token
    send_mail(
        subject,
        body,
        'noreply@aeonem.xyz',
        [profile.user.email],
        fail_silently=False,
    )


def send_new_account_activation_email(profile: espn_models.Profile):
    subject = 'Account Activation Token'
    body = create_new_access_token(profile)
    send_mail(
        subject,
        body,
        'noreply@aeonem.xyz',
        [profile.user.email],
        fail_silently=False,
    )
