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
def get_comment_field(request, commented_id, profile=None, logged_in=False):
    commented_type = request.GET['type']
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


@find_profile_decorator
def like_comment(request, comment_id: int, profile: espn_models.Profile):
    try:
        comment = comment_models.Comment.objects.get(id=comment_id)
        try:
            comment_models.CommentLike.objects.get(
                profile=profile,
                comment=comment
            )
            return JsonResponse(
                data={
                    'ok': False,
                    'description': 'You Can\'t like an item twice'
                }
            )
        except:
            like = comment_models.CommentLike()
            like.comment = comment
            like.profile = profile
            like.save()
            return JsonResponse(
                data={
                    'ok': True,
                    'description': 'Comment was liked successfully'
                }
            )
    except:
        return JsonResponse(
            data={
                'ok': False,
                'description': 'Unable to like comment'
            }
        )
