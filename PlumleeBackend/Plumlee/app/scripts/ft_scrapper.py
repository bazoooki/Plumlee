import requests
import json
import time
import sys, os
import django
from app.models import *

# http://dreamteam.sport5.co.il/API/Rank/League/1?GUID=100033
LEAGUE = '?GUID=100033' # wobbi main league
URL = 'http://dreamteam.sport5.co.il/API/Rank/League/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
  'Cache-Control': 'max-age=0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Encoding': 'gzip, deflate, sdch',
  'Accept-Language': 'en-US,en;q=0.8'

}

page_num = 1
total_pages = 99

def get_url(URL):
  return requests.get(URL, headers = headers)

def get_league_teams():
  i = page_num -1
  while i < page_num+total_pages:
    page = i+1
    print(page)
    full_url = URL + str(page) + LEAGUE
    data = get_url(full_url)
    text = data.text  
    teams = json.loads(text)  
    for team in teams['table']:
      user_id = team['userId']
      get_teams_data(user_id)
    time.sleep( 2 )
    i += 1    
  

def get_teams_data(user_id):
  TEAM_URL = 'http://dreamteam.sport5.co.il/API/Team/GetSomeoneTeam/' + str(user_id)
  data = get_url(TEAM_URL)
  text = data.text  
  team_data = json.loads(text)  
  players = team_data['players']
  team_name = team_data['teamName']
  team_total_score = team_data['teamPoints']
  team_id = user_id  
  allowed_subs = team_data['allowedSubs']
  subs_made = team_data['subsMade']
  remaining_budget = team_data['remainingBudget']
  coach_name = team_data['coachName']
  if FantasyTeam.objects.filter(team_id=team_id).exists():
    team = FantasyTeam.objects.filter(team_id=team_id).first()
    print('team already exists:', user_id)    
    team = None
    return
  else:
    team = FantasyTeam(
      team_name=team_name,
      team_total_score=team_total_score,
      team_id=team_id,    
      allowed_subs=allowed_subs,
      subs_made=subs_made,    
      remaining_budget=remaining_budget,
      coach_name=coach_name
    )
    team.save()
    for player in players:
      player_id = player['id']
      player_name = player['name']
      is_captain = player['isCaptain']      
      player = Player.objects.filter(player_id=player_id).first()      
      if player is not None:
        team.players.add(player)
        if is_captain:
          print('adding captain ', player)
          team.captain = player
    
    team.save()
  print('finish giving data for team', team_name)

def import_fteam_players():
  get_league_teams()


