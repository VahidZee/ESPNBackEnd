# General Imports
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password

# Local Imports
from Espn import models as espn_models
from Espn import methods as espn_methods


# Create your views here.
def login(request) -> JsonResponse:
    try:
        profile = espn_models.Profile.objects.get(user__username__exact=request.POST['username'])
        if not check_password(password=request.POST['password'], encoded=profile.user.password):
            return espn_methods.user_password_was_incorrect()
    except Exception:
        return espn_methods.user_profile_not_found()
    token = espn_methods.create_new_access_token(profile)
    return JsonResponse(data={
        'ok': True,
        'token': token
    })

def logon(request):
    try:
        profile = espn_models.Profile.objects.get(user__username__exact=request.POST['username'])
        if not check_password(password=request.POST['password'], encoded=profile.user.password):
            return espn_methods.user_password_was_incorrect()
    except Exception:
        return espn_methods.user_profile_not_found()
    token = espn_methods.create_new_access_token(profile)
    return JsonResponse(data={
        'ok': True,
        'token': token
    })