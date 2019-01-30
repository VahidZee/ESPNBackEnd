from django.shortcuts import render
from ESPNBackEnd.Game.models import Player, Team, Match
from django.http import HttpResponse
import json


def send_player_data(_, p_id):
    player = Player.objects.get(id=p_id)

    json_dict = player.json_dict()

    http_response = HttpResponse(
        json.dumps(
            json_dict,
        ),
        content_type='application/json',
    )
    http_response.status_code = 200
    return http_response


def send_team_data(_, t_id):
    send_regular_data(Team, t_id)


def send_game_data(_, g_id):
    send_regular_data(Match, g_id)


def send_regular_data(model_obj, id):
    try:
        model = model_obj.objects.get(id)

        json_dict = model.json_dict()

        http_response = HttpResponse(
            json.dumps(
                json_dict,
            ),
            content_type='application/json'
        )

        http_response.status_code = 200
        return http_response
    except Exception as e:
        http_response = HttpResponse(
            json.dumps(
                {
                    'error': 'unable to create json dict'
                }
            ),
            content_type='application/json'
        )

        http_response.status_code = 400
        return http_response
