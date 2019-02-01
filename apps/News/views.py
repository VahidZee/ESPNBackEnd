# General Imports
from django.http import HttpResponse, JsonResponse

from datetime import datetime, timedelta

import json

# Model Imports
import apps.News.models as news_models
from apps.Espn import models as espn_models

# Local Imports
from apps.Espn import methods as espn_methods

# Constant Values
PAGE_POSTS_COUNT = 4


# Create your views here.
def get_news_by_id(request, news_id: int):
    try:
        news = news_models.News.objects.get(id=news_id)

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

    news = news_models.News.objects.all().order_by('-uploaded_at')
    response_json_array = []
    response = {
        'ok': True,
        'description': '',
        'has_more': False,
        'list': [],
    }
    temp_array = []

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

        # response payload
        response['list'] = response_json_array

        # response pagination
        if page_number * PAGE_POSTS_COUNT < news.count():
            response['has_more'] = True

    # Filtering Subscribed Option
    if get_type == 'subscribed':
        if not logged_in:
            response['ok'] = False
            response['description'] = 'You need to be logged in to see your subscribed news'
            return JsonResponse(
                data=response
            )

    # Filtering and Finding related News
    if get_type == 'related':
        data = json.loads(request.body)
        for related_tag in data['tags']:
            tag = news_models.NewsTag.objects.get(
                tag_title=related_tag['title'],
                tagged_id=related_tag['id'],
                tag_type=related_tag['type']
            )
            related_news = news.filter(newstag=tag)
            for temp_news in related_news:
                temp_array.append(
                    temp_news.summery_json_dict()
                )
            # response payload
            response_json_array = temp_array[(page_number - 1) * PAGE_POSTS_COUNT: page_number * PAGE_POSTS_COUNT - 1]

            # response pagination
            response['list'] = response_json_array

            # Response Pagination
            if len(temp_array) > page_number * PAGE_POSTS_COUNT:
                response['has_more'] = True

    return JsonResponse(
        data=response
    )
