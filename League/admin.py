from django.contrib import admin

from ESPNBackEnd.League.models import Tournament, TeamResult, RowTournament, League

admin.site.register(League)
admin.site.register(Tournament)
admin.site.register(TeamResult)
admin.site.register(RowTournament)
