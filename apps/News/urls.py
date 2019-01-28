from django.urls import path
from .views import get_news_by_id, get_news_list

urlpatterns = [
    path('', get_news_list),
    path('<int:news_id>', get_news_by_id),
]
