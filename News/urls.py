from django.urls import path
from .views import get_news_by_id

urlpatterns = [
    path('<int:news_id>', get_news_by_id),
]
