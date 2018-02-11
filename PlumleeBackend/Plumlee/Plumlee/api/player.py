from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from app.models import *
import datetime


@csrf_exempt
def get_all_players(request):

    ret = {'status': 'FAIL'}
    ret['players'] = []
    if request.method == 'GET':        

        players = Player.objects.all()
        for player in players:
            selected_by = player.teams.count()
            capatain_by = player.teams_captain.count()
            teams_captain = player.teams_captain.all()
            teams = []
            for team in teams_captain:
                teams.append({
                    'team_name': team.team_name,
                    'id': team.team_id,
                    'team_total_score': team.team_total_score
                })
            player_data = {
                'player_id': player.player_id,
                'player_name': player.player_name,                
                'team': player.team.team_name,
                'player_market_value': player.player_market_value,
                'position': player.position,
                'points_value': player.points_value,
                'is_suspended': player.is_suspended,
                'is_injured': player.is_suspended,
                'is_missing': player.is_suspended,
                'selected_by': selected_by,
                'captain_by': capatain_by,
                'teams_captain': teams
            }
            ret['status'] = 'OK'
            ret['players'].append(player_data)

    return JsonResponse(ret)

    



