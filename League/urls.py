from django.urls import path
from ESPNBackEnd.League import views

urlpatterns = [
    path('player/<int:l_id>', views.send_league_data),
    path('', views.send_game_data),
]