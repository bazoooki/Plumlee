from django.db import models

# Create your models here.
class Team(models.Model): 
  team_name = models.CharField(max_length=100, blank=True)
  team_num = models.IntegerField(blank=True)
  team_flag_pic = models.CharField(max_length=100, blank=True)
  shirt_picture = models.CharField(max_length=100, blank=True)

  class Meta:
    db_table = 'team' 

  @staticmethod
  def get_or_create(data):

    team_name = data.get('team_name')
    team_num = data.get('team_num')    
    team_flag_pic = data.get('team_flag_pic')
    shirt_picture = data.get('shirt_picture')
    if team_flag_pic == None:
      team_flag_pic = ''
    if shirt_picture == None:
        shirt_picture = ''
    if team_name == None or team_num == None:
      print('None')
      return None
    # check if team exists - retun team
    if Team.objects.filter(team_num = team_num).exists():
      team = Team.objects.filter(team_num = team_num).first()
    # if not - add player to database
    else:
      print('else!')
      team = Team(
        team_name = team_name,
        team_num = team_num,
        team_flag_pic = team_flag_pic,
        shirt_picture = shirt_picture
      )
      team.save()
    return team

  def __str__(self):
    return self.team_name

class Player(models.Model):
  player_id = models.IntegerField(blank=True)
  player_name = models.CharField(max_length=100, blank=True)
  position = models.CharField(max_length=2, blank=True)
  team = models.ForeignKey(Team, related_name='team')
  player_market_value = models.IntegerField(blank=True)
  points_value = models.FloatField(blank=True, default = 0)
  is_suspended = models.BooleanField(default=False)
  is_injured = models.BooleanField(default=False)
  is_missing = models.BooleanField(default=False)


  class Meta:
    db_table = 'player' 

  @staticmethod
  def get_or_create(data):    
    player_id = data.get('player_id')
    player_name = data.get('player_name')
    position = data.get('position')
    team  = Team.get_or_create(data)    
    player_market_value = data.get('player_market_value')
    points_value = data.get('points_value')
    is_suspended = data.get('is_suspended')
    is_injured = data.get('is_injured')
    is_missing = data.get('is_missing')
    if player_id == None or player_name == None:
      return None
    player = None
    # check if player exists - retun player
    if Player.objects.filter(player_id=player_id).exists():
      player = Player.objects.filter(player_id=player_id).first()
    # if not - add player to database
    else:
      print('adding new player')
      player = Player(
        player_id=player_id,
        player_name=player_name,
        position=position,
        team=team,
        player_market_value=player_market_value,
        points_value=points_value,
        is_suspended=is_suspended,
        is_injured=is_injured,
        is_missing=is_missing
      )
      player.save()
      print('added')
    return player

  def __str__(self):
    return self.player_name


class FantasyTeam(models.Model):
  team_name = models.CharField(max_length=100, blank=True)
  team_total_score = models.CharField(max_length=100, blank=True)
  team_id = models.IntegerField(blank=True)  
  players = models.ManyToManyField(Player, related_name="teams")
  allowed_subs = models.FloatField(blank=True, default = 0)
  subs_made = models.FloatField(blank=True, default = 0)
  remaining_budget = models.FloatField(blank=True, default = 0)
  coach_name = models.CharField(max_length=100, blank=True)
  captain = models.ForeignKey(Player, null=True, related_name='teams_captain')
  # owner = models.ForeignKey(User, related_name='user_teams',  blank=True)

  def __str__(self):
    return self.team_name  
# teamName,teamPoints,allowedSubs,coachName,favTeamId, remainingBudget,subsMade,updatedOn
