from django.contrib import admin
from .models import *

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'position', 'team', 'player_market_value')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_num', 'team_flag_pic')


@admin.register(FantasyTeam)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'team_name', 'team_total_score')    
