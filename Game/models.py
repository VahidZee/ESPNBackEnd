from django.db import models


# class RangeField(models.IntegerField):
#     def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value':self.max_value}
#         defaults.update(kwargs)
#         return super(RangeField, self).formfield(**defaults)

class Team(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    players = models.ForeignKey(to=Player, on_delete=models.CASCADE)


class Stat(models.Model):
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


class Player(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE)
    stats = models.ForeignKey(to=Stat, on_delete=models.CASCADE)
    BASKET_PLAYER = 'BASKET'
    FOOTBALL_PLAYER = 'FOOT'
    types = (
        (BASKET_PLAYER, 'basketball'),
        (FOOTBALL_PLAYER, 'football'),
    )
    ATTACK = 'ATTACK'
    DEFENCE = 'DEFENCE'
    GOAL_KEEPER = 'GOAL'
    # TODO learn the basketball and football posts and complete the posts choices
    posts = (
        (ATTACK, 'attack'),
        (DEFENCE, 'defence'),
        (GOAL_KEEPER, 'goal keeper'),

    )
    sport_type = models.CharField(choices=types, max_length=10)
    post = models.CharField(choices=posts, max_length=100)


class Report(models.Model):
    time = models.TimeField()
    explain = models.TextField()


class Event(models.Model):
    CORNER = 'CORNER'
    # TODO: fill the event_choices with related data
    types = (
        (CORNER, 'corner'),
    )
    event_type = models.CharField(choices=types, max_length=100)
    related_player = models.ForeignKey(to=Player, on_delete=models.PROTECT, blank=True)
    time = models.TimeField()
    explanation = models.TextField()


class MediaImage(models.Model):
    image = models.ImageField()


class MediaVideo(models.Model):
    # video field shit...
    pass


class Match(models.Model):
    BASKETBALL = 'BASKET'
    FOOTBALL = 'FOOT'
    types = (
        (BASKETBALL, 'basketball'),
        (FOOTBALL, 'football'),
    )
    team_f = models.ForeignKey(to=Team, on_delete=models.CASCADE)
    team_s = models.ForeignKey(to=Team, on_delete=models.CASCADE)
    score_f = models.IntegerField(default=0)
    score_s = models.IntegerField(default=0)
    date = models.DateField()
    sport_type = models.CharField(choices=types, max_length=10)
    events = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    time_report = models.ForeignKey(to=Report, on_delete=models.CASCADE)
    image_medias = models.ForeignKey(to=MediaImage, on_delete=models.CASCADE)
    video_medias = models.ForeignKey(to=MediaVideo, on_delete=models.CASCADE)

    def get_winner(self):
        if self.score_s > self.score_f:
            return self.team_s
        elif self.score_s < self.score_f:
            return self.team_f
        else:
            return None
