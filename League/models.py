from django.db import models
# from Game.models import Match, Team


# class TeamResult(models.Model):
#     team = models.ForeignKey(to=Team, on_delete=models.PROTECT)
#     score = models.IntegerField(default=0)
#     games = models.IntegerField(default=0)
#
#
# class RowTournament(models.Model):
#     matches = models.ForeignKey(to=Match, on_delete=models.PROTECT)
#
#
# class Tournament(models.Model):
#     # first row contains 8 matches
#     # first_row = models.OneToOneField(RowTournament, blank=True, on_delete=models.CASCADE)
#     # # second row contains 4 matches
#     # second_row = models.OneToOneField(RowTournament, blank=True, on_delete=models.CASCADE)
#     # # third row contains 2 matches
#     # third_row = models.OneToOneField(RowTournament, blank=True, on_delete=models.CASCADE)
#     # # fourth row contains final match
#     # fourth_row = models.OneToOneField(RowTournament, blank=True, on_delete=models.CASCADE)
#
#
# class League(models.Model):
#     matches = models.ForeignKey(Match, on_delete=models.PROTECT)
#     teams = models.ForeignKey(TeamResult, on_delete=models.PROTECT, blank=True)
#     tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
