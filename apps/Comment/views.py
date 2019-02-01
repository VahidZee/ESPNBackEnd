# General Imports
from django.http import JsonResponse

# Models Imports
from . import models as comment_models
from apps.Espn import models as espn_models

# Local imports
from apps.Espn.methods import find_profile_decorator, find_profile_if_exists_decorator

# Constant Values
POSTS_PER_PAGE = 1


@find_profile_if_exists_decorator
def get_comment_field(request, id, profile=None, logged_in=False):
    commented_type = request.GET['type']
    commented_id = id
    try:
        page_number = int(request.GET['page'])
    except Exception:
        page_number = 1

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
        comments = comments.filter(reply_to__isnull=True)
        response_list = [comment.comment_json_dict(profile) for comment in comments]

        # Paginating Response
        response['list'] = response_list[(page_number - 1) * POSTS_PER_PAGE: page_number * POSTS_PER_PAGE]
        if len(response_list) > page_number * POSTS_PER_PAGE:
            response['has_more'] = True

    return JsonResponse(
        data=response
    )
