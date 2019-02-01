from apps.League import League
from django.http import HttpResponse
import json


def send_league_data(_, l_id):
    try:
        league = League.objects.get(l_id)

        json_dict = league.json_dict()

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


def send_leagues(request):
    leagues = League.objects.all()
    response = {}
    for league in leagues:
        response.append(
            league.pre_json()
        )
    http_response = HttpResponse(
        json.dumps(
            response
        )
    )

    http_response.status_code = 200
    return http_response
