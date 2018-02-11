import requests
import json
import sys, os
import django
from app.models import *


URL = 'http://dreamteam.sport5.co.il/API/Player/Get'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
  'Cache-Control': 'max-age=0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Encoding': 'gzip, deflate, sdch',
  'Accept-Language': 'en-US,en;q=0.8'

}

def get_url(URL):
  return requests.get(URL, headers = headers)

def get_players():
  data = get_url(URL)
  text = data.text
  text = text.replace('\"', '"')
  players_list = json.loads(text)
  players_list = json.loads(players_list)
  for player in players_list:
    print(player)
    player_data = {}
    player_data['team_name'] = player.get('teamName')
    player_data['team_num']  = player.get('teamNum')
    player_data['shirt_picture']  = player.get('shirtPicture')
    player_data['team_flag_pic']  = player.get('teamFlagPic')    
    player_data['player_id'] = player.get('id')    
    player_data['player_name'] = player.get('name')
    player_data['position'] = player.get('type')
    player_data['player_market_value'] = player.get('marketValue')
    player_data['points_value'] = player.get('pointsValue')
    player_data['is_suspended'] = player.get('isSuspended')
    player_data['is_injured'] = player.get('isInjured')    
    player_data['is_missing'] = player.get('isMissing')  
    player = Player.get_or_create(player_data)      

def import_data():
  get_players()


