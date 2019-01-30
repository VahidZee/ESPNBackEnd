from django.urls import path
from ESPNBackEnd.Game import views

urlpatterns = [
    path('player/<int:p_id>', views.send_player_data),
]
