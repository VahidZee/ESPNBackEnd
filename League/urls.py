from django.urls import path
from django.http import JsonResponse


def index(request):
    return JsonResponse()
urlpatterns = [
    path('',  index)
]