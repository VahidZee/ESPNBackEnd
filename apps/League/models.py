from django.db import models
# from apps.Game.models import Match
import datetime

UPCOMING = 'upcoming'
IN_PROCESS = 'in process'
FINISHED = 'finished'


class League(models.Model):
    # name = models.CharField(max_length=1000)
    # matches = models.ForeignKey(Match, on_delete=models.PROTECT)
    # date = models.DateTimeField()
    # finished = models.BooleanField(default=False)
    #
    # def compare_date(self):
    #     if self.finished:
    #         return FINISHED
    #     if datetime.now < self.date:
    #         return UPCOMING
    #     return IN_PROCESS
    #
    # def json_dict(self):
    #     matches = list()
    #     for match in self.matches.all():
    #         matches.append(
    #             match.prev_json()
    #         )
    #
    #     team_res = list()
    #     for team in self.teams.all():
    #         team_res.append(
    #             team.prev_json()
    #         )
    #
    #     tournament = list()
    #     for tour in self.tournament.all():
    #         tournament.append(
    #             tour.json_dict()
    #         )
    #         break
    #
    #     json_dict = {
    #         'name': self.name,
    #         'matches': matches,
    #         'teams': team_res,
    #         'tournament': tournament,
    #         'date': self.date,
    #         'status': self.compare_date(),
    #         'league_id': self.id
    #     }
    #     return json_dict
    #
    # def pre_json(self):
    #     pre_json = {
    #         'name': self.name,
    #         'status': self.compare_date(),
    #         'id': self.id,
    #         'date': self.date,
    #     }
    #     return pre_json
    pass

class TeamResult(models.Model):
    # league = models.ForeignKey(to=League, on_delete=models.CASCADE)
    # score = models.IntegerField(default=0)
    # games = models.IntegerField(default=0)
    #
    # def json_dict(self):
    #     teams = list()
    #     for team in self.team_set.all():
    #         teams.append(
    #             team.prev_json()
    #         )
    #         break
    #
    #     json_dict = {
    #         'score': self.score,
    #         'games': self.games,
    #         'team': teams
    #     }
    #     return json_dict
    pass


class RowTournament(models.Model):
    #
    # def get_list(self, number):
    #     matches = list()
    #
    #     for index, match in enumerate(self.match_set.all()):
    #         if index == number:
    #             break
    #         matches.append(
    #             match.prev_json()
    #         )
    #         break
    #     return matches
    # league = models.ForeignKey(to=League, on_delete=models.CASCADE)
    # # first row contains 8 matches
    # first_row = models.OneToOneField(RowTournament, blank=True)
    # # second row contains 4 matches
    # second_row = models.OneToOneField(RowTournament, blank=True)
    # # third row contains 2 matches
    # third_row = models.OneToOneField(RowTournament, blank=True)
    # # fourth row contains final match
    # fourth_row = models.OneToOneField(RowTournament, blank=True)
    #
    # def json_dict(self):
    #     first = self.first_row.get_list(8)
    #     second = self.second_row.get_list(4)
    #     third = self.third_row.get_list(2)
    #     fourth = self.fourth_row.get_list(1)
    #     # for index, item in enumerate(self.first_row.all()):
    #     #     if index == 8:
    #     #         break
    #     #     first.append(
    #     #         item.json_dict()
    #     #     )
    #     #
    #     # second = list()
    #     # for index, item in enumerate(self.second_row.all()):
    #     #     if index == 4:
    #     #         break
    #     #     second.append(
    #     #         item.json_dict()
    #     #     )
    #     #
    #     # third = list()
    #     # for index, item in enumerate(self.third_row.all()):
    #     #     if index == 2:
    #     #         break
    #     #     third.append(
    #     #         item.json_dict()
    #     #     )
    #     #
    #     # fourth = list()
    #     # for item in self.fourth_row.all():
    #     #     fourth.append(
    #     #         item.json_dict()
    #     #     )
    #     #     break
    #     json_dict = {
    #         'first': first,
    #         'second': second,
    #         'third': third,
    #         'fourth': fourth
    #     }
    #     return json_dict
    pass


class Tournament(models.Model):
    pass
