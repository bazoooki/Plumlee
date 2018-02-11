from django.core.management.base import BaseCommand, CommandError
from app.scripts.ft_scrapper import get_league_teams
class Command(BaseCommand):
    help = 'Pulls fantasy team players'

    def handle(self, *args, **options):
        get_league_teams()