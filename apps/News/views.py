# General Imports
from django.http import HttpResponse, JsonResponse
import json

# Model Imports
from .models import News

# Constant Values
PAGE_POSTS_COUNT = 4


# Create your views here.
def get_news_by_id(request, news_id):
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


def get_news_list(request):
    get_type = request.GET['type']
    try:
        page_number = int(request.GET['page'])
    except Exception:
        page_number = 1

    news = News.objects.all().filter()
    response_json_array = []
    if get_type == 'recent':
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
    if page_number * PAGE_POSTS_COUNT <= news.count():
        response['has_more'] = True

    http_response = HttpResponse(
        json.dumps(
            response
        ),
        content_type='application/json',
    )
    http_response.status_code = 200
    return http_response
