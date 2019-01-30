from django.urls import path
from ESPNBackEnd.Game import views

urlpatterns = [
    path('player/<int:p_id>', views.send_player_data),
    path('game/<int:g_id>', views.send_game_data),
    path('team/<int:t_id>', views.send_team_data),
]
