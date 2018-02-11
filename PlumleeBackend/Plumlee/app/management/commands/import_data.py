from django.core.management.base import BaseCommand, CommandError
from app.scripts.scrapper import get_players
class Command(BaseCommand):
    help = 'Pulls data'

    def handle(self, *args, **options):
        get_players()