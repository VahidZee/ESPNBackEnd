from django.shortcuts import render
from django.http import HttpResponse
from .models import News
import json


# Create your views here.
def get_news_by_id(request, news_id):
    news = News.objects.get(id=news_id)

    json_dict = news.json_dict()

    http_response = HttpResponse(
        json.dumps(
            json_dict,
            many=True,
        ),
        content_type='application/json',
    )
    http_response.status_code = 200
    return http_response


def get_news_list(request):
    get_type = request.GET['type']
    news = News.objects.all()
    response_json_array = []
    if get_type == 'recent':
        for n in news:
            response_json_array.append(
                n.summery_json_dict()
            )

    http_response = HttpResponse(
        json.dumps(
            response_json_array,
        ),
        content_type='application/json',
    )
    http_response.status_code = 200
    return http_response
