from django.shortcuts import render
from django.http import HttpResponse
from .models import News
import json


# Create your views here.
def get_news_by_id(request, news_id):
    news = News.objects.get(id=news_id)

    images = list()
    for image in news.newsimage_set.all():
        images.append(
            {
                'image': 'http://localhost:8000/' +  str(image.image.url),
                'caption': str(image.image_title),
                'text': str(image.image_description)
            }
        )

    tags = list()
    for tag in news.newstag_set.all():
        tags.append(
            {
                'type': tag.tag_type,
                'id': tag.tagged_id,
                'title': tag.tag_title
            }
        )

    resources = list()
    for resource in news.newsresource_set.all():
        resources.append(
            {
                'title': resource.resource_title,
                'link': resource.resource_url
            }
        )
    response = {
        'id': news_id,
        'backgroundImage' :  'http://localhost:8000/' +  str(news.background_image.url),
        'title': news.news_title,
        # TODO add logic
        'isSubscribed': False,
        'paragraphs': news.news_text.split('\n'),
        'images': images,
        'resources': resources,
        'tags': tags,
        'publishDate': news.uploaded_at.isoformat()
    }

    http_response = HttpResponse(json.dumps(
        response,
    ),
        content_type='application/json',

    )
    http_response.status_code = 200
    return http_response
