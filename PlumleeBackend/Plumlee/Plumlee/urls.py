
from django.conf.urls import url
from django.contrib import admin
from Plumlee.api import player, users


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/players/get$', player.get_all_players),
    url(r'^api/login$', users.login_view),
    url(r'^api/register$', users.register_view),
    url(r'^api/logout$', users.logout_view),
    url(r'^api/whoami$', users.whoami)
]
