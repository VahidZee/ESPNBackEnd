# General Imports
from django.http import JsonResponse

from django.contrib.auth.hashers import check_password

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from datetime import datetime

# Models Imports
from django.contrib.auth.models import User
from Espn import models as espn_models
# Local Imports
from Espn import methods as espn_methods


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
def login(request) -> JsonResponse:
    try:
        profile = espn_models.Profile.objects.get(user__username__exact=request.POST['username'])
        if not check_password(password=request.POST['password'], encoded=profile.user.password):
            return espn_methods.user_password_was_incorrect()
    except Exception:
        print(request.body)
        print(request.POST['username'])
        return espn_methods.user_profile_not_found()
    token = espn_methods.create_new_access_token(profile)
    profile.user.last_login = datetime.now()
    profile.save()
    return JsonResponse(data={
        'ok': True,
        'token': token
    })


@method_decorator(csrf_exempt, name='dispatch')
def logon(request):
    try:
        if User.objects.all().filter(username__exact=request.POST['username']).count() == 0:
            user = User()
            user.username = request.POST['username']
            user.password = request.POST['password']
            user.email = request.POST['email']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            profile = espn_models.Profile(user=user)
            profile.save()
        else:
            return JsonResponse(
                data={
                    'ok': False,
                    'description': 'Username was taken'
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
