# General Imports
from django.http import HttpResponse, JsonResponse

from datetime import datetime, timedelta

import json

# Model Imports
from .models import News
from apps.Espn import models as espn_models

# Local Imports
from apps.Espn import methods as espn_methods

# Constant Values
PAGE_POSTS_COUNT = 4


# Create your views here.
def get_news_by_id(request, news_id: int):
    try:
        news = News.objects.get(id=news_id)

        json_dict = news.json_dict()

        http_response = HttpResponse(
            json.dumps(
                json_dict,
            ),
            content_type='application/json',
        )
        http_response.status_code = 200
        return http_response
    except Exception:
        response = JsonResponse(
            data={
                'ok': False,
                'description': 'News Was Not Found'
            }
        )
        response.status_code = 404
        return response


@espn_methods.find_profile_if_exists_decorator
def get_news_list(request, profile, logged_in: bool = False):
    # Getting Filter Type
    get_type = request.GET['type']
    try:
        page_number = int(request.GET['page'])
    except Exception:
        page_number = 1

    news = News.objects.all()
    response_json_array = []

    # Filtering Recent Option
    if get_type == 'recent':
        news = news.filter(uploaded_at__gte=datetime.now() - timedelta(days=2))
        for index in range((page_number - 1) * PAGE_POSTS_COUNT, page_number * PAGE_POSTS_COUNT):
            if index < news.count():
                response_json_array.append(
                    news[index].summery_json_dict()
                )
            else:
                break
    response = {
        'list': response_json_array,
        'has_more': False
    }

    # Response Pagination
    if page_number * PAGE_POSTS_COUNT < news.count():
        response['has_more'] = True
    print(response)
    return JsonResponse(
        data=response
    )
