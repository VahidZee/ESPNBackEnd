from django.shortcuts import render
from django.http import HttpResponse
from .models import News
import json

PAGE_POSTS_COUNT = 4


# Create your views here.
def get_news_by_id(request, news_id):
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


def get_news_list(request):
    get_type = request.GET['type']
    try:
        page_number = int(request.GET['page'])
    except Exception:
        page_number = 1

    news = News.objects.all()
    response_json_array = []
    if get_type == 'recent':
        for index in range((page_number - 1) * PAGE_POSTS_COUNT, (page_number) * PAGE_POSTS_COUNT):
            if index < news.count():
                response_json_array.append(
                    news[index].summery_json_dict()
                )
            else:
                break

    http_response = HttpResponse(
        json.dumps(
            response_json_array,
        ),
        content_type='application/json',
    )
    http_response.status_code = 200
    return http_response
