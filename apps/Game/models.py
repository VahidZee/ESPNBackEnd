from django.db import models
from apps.League.models import TeamResult, RowTournament


# class RangeField(models.IntegerField):
#     def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value':self.max_value}
#         defaults.update(kwargs)
#     return super(RangeField, self).formfield(**defaults)

class Match(models.Model):
    row_tour = models.ForeignKey(to=RowTournament, on_delete=models.CASCADE)
    BASKETBALL = 'BASKET'
    FOOTBALL = 'FOOT'
    types = (
        (BASKETBALL, 'basketball'),
        (FOOTBALL, 'football'),
    )
    score_f = models.IntegerField(default=0)
    score_s = models.IntegerField(default=0)
    date = models.DateField()
    sport_type = models.CharField(choices=types, max_length=10)

    # tables and timeline are created by this field
    # this field is for the time report

    def get_winner(self):
        if self.score_s > self.score_f:
            return self.team_s
        elif self.score_s < self.score_f:
            return self.team_f
        else:
            return None

    def json_dict(self):
        teams = self.team_set.all()
        team_f = teams[0]
        team_s = teams[1]

        events = list()
        for event in self.event_set.all():
            events.append(
                event.json_dict()
            )

        time_report = list()
        for report in self.report_set.all():
            time_report.append(
                report.json_dict()
            )

        images = list()
        for img in self.mediaimage_set.all():
            images.append(
                img.json_dict()
            )

        videos = list()
        for video in self.mediavideo_set.all():
            videos.append(
                video.json_dict()
            )
        json_dict = {
            'team_f': team_f,
            'team_s': team_s,
            'sport': self.sport_type,
            'score_f': self.score_f,
            'score_s': self.score_s,
            'date': self.date,
            'events': events,
            'time_report': time_report,
            'images': images,
            'videos': videos,
        }
        return json_dict

    def prev_json(self):
        json_dict = {
            'team_f': {
                'name': self.team_f.name,
                'id': self.team_f.id,
            },
            'team_s': {
                'name': self.team_s.name,
                'id': self.team_s.id
            },
            'score_f': self.score_f,
            'score_s': self.score_s

        }
        return json_dict


class Team(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    match = models.ForeignKey(to=Match, on_delete=models.CASCADE)
    result = models.ForeignKey(to=TeamResult, on_delete=models.PROTECT)

    def json_dict(self):
        players = list()
        for player in self.players:
            players.append(
                player.json_dict()
            )
        json_dict = {
            'name': self.name,
            'players': players
        }
        return json_dict

    def prev_json(self):
        players = list()
        for player in self.players:
            players.append(
                player.prev_json()
            )
        json_dict = {
            'name': self.name,
            'players': self.players
        }
        return json_dict


class Player(models.Model):
    team = models.ForeignKey(to=Team, on_delete=models.PROTECT, default=None)
    name = models.CharField(max_length=1000, unique=True)
    BASKET_PLAYER = 'BASKET'
    FOOTBALL_PLAYER = 'FOOT'
    types = (
        (BASKET_PLAYER, 'basketball'),
        (FOOTBALL_PLAYER, 'football'),
    )
    ATTACK = 'ATTACK'
    DEFENCE = 'DEFENCE'
    GOAL_KEEPER = 'GOAL'
    BEST_PLAYER = 'BEST'
    BRANCH_PLAYER = 'BRANCH'
    # TODO learn the basketball and football posts and complete the posts choices
    posts = (
        (ATTACK, 'attack'),
        (DEFENCE, 'defence'),
        (GOAL_KEEPER, 'goal keeper'),

    )
    sport_type = models.CharField(choices=types, max_length=10)
    post = models.CharField(choices=posts, max_length=100)
    born = models.DateField()
    experience = models.IntegerField()

    def json_dict(self):
        stat_list = list()
        for stat in self.stat_set.all():
            stat_list.append(
                stat.json_dict()
            )
        json_dict = {
            'sport': self.sport_type,
            'post': self.post,
            'id': self.id,
            'stats': stat_list,
            'name': self.name,
            'team_name': self.team.name,
            'born': self.born.isoformat(),
            'exp': self.experience,
        }
        return json_dict

    def prev_json(self):
        json_dict = {
            'id': self.id,
            'name': self.name,
        }
        return json_dict


class Stat(models.Model):
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE, default=None)
    season = models.IntegerField(unique=True)
    GP = models.IntegerField()
    MPG = models.IntegerField()
    FG = models.IntegerField()
    APG = models.IntegerField()
    RPG = models.IntegerField()
    BLKPG = models.IntegerField()
    STPG = models.IntegerField()
    PFPG = models.IntegerField()
    PPG = models.IntegerField()

    def json_dict(self):
        json_dict = {
            'season': self.season,
            'GP': self.GP,
            'MPG': self.MPG,
            'FG': self.FG,
            'APG': self.APG,
            'RPG': self.RPG,
            'BLKPG': self.BLKPG,
            'STPG': self.STPG,
            'PFPG': self.PFPG,
            'PPG': self.PPG
        }

        return json_dict


class Report(models.Model):
    time = models.TimeField()
    explain = models.TextField()
    match = models.ForeignKey(to=Match, on_delete=models.CASCADE)

    def json_dict(self):
        json_dict = {
            'time': self.time,
            'explain': self.explain
        }
        return json_dict


class Event(models.Model):
    match = models.ForeignKey(to=Match, on_delete=models.CASCADE)
    CORNER = 'CORNER'
    HAND = 'HAND'
    # TODO: fill the event_choices with related data
    types = (
        (CORNER, 'corner'),
        (HAND, 'hand'),
    )
    event_type = models.CharField(choices=types, max_length=100)
    related_player = models.ForeignKey(to=Player, on_delete=models.PROTECT, blank=True)
    time = models.TimeField()
    explanation = models.TextField()

    def json_dict(self):
        players = list()
        for player in self.related_player.all():
            players.append(
                player.json_dict()
            )
        json_dict = {
            'event': self.event_type,
            'players': players,
            'time': self.time,
            'explanation': self.explanation
        }
        return json_dict


class MediaImage(models.Model):
    image = models.ImageField()
    match = models.ForeignKey(to=Match, on_delete=models.CASCADE)

    def json_dict(self):
        pass


class MediaVideo(models.Model):
    match = models.ForeignKey(to=Match, on_delete=models.CASCADE)
    url = models.URLField()

    def json_dict(self):
        return {
            'url': self.url
        }
