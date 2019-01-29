from django.db import models
from ESPNBackEnd.Game.models import Match, Team


class TeamResult(models.Model):
    team = models.ForeignKey(to=Team)
    score = models.IntegerField(default=0)
    games = models.IntegerField(default=0)


class Tournament(models.Model):
    pass


class League(models.Model):
    matches = models.ForeignKey(Match)
    teams = models.ForeignKey(TeamResult)
