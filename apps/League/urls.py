from django.urls import path
from apps.League import views

urlpatterns = [
    path('player/<int:l_id>', views.send_league_data),
    path('', views.send_leagues),
]
