# General Imports
from django.http import JsonResponse

# Models Imports
from . import models as comment_models
from apps.Espn import models as espn_models

# Local imports
from apps.Espn.methods import find_profile_decorator

# Constant Values
POSTS_PER_PAGE = 4


def get_comment_field(request):
    commented_type = request.GET['type']
    commented_id = request.GET['id']
    page_number = request.GET['page_number']
    response = {
        'ok': True,
        'has_more': False,
        'description': '',
        'list': [],
    }

    try:
        comment_field = comment_models.CommentField.objects.get(
            commented_id=commented_id,
            field_type=commented_type,
        )
    except Exception:
        return JsonResponse(
            data={
                'ok': False,
                'description': 'Comment Field couldn\'t be found!'
            }
        )
    else:
        comments = comment_field.comment_set.order_by('-uploaded_at')