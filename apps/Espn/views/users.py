# general imports
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# model imports
from apps.Espn.models import Profile

# local imports
from apps.Espn.methods import find_profile_decorator


@find_profile_decorator
def get_me(request, profile: Profile) -> JsonResponse:
    response_dict = {
        'username': profile.user.username,
        'first_name': profile.user.first_name,
        'last_name': profile.user.last_name,
        'profile_picture': profile.profile_picture.url,
    }
    return JsonResponse(
        data=response_dict
    )
