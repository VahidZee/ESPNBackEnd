# General Imports
from django.db import models

# Model Imports
from apps.Espn import models as espn_models


# Local Imports

class CommentField(models.Model):
    GAME_TYPE = 'G'
    TEAM_TYPE = 'T'
    PLAYER_TYPE = 'P'
    LEAGUE_TYPE = 'L'
    NEWS_TYPE = 'N'
    FIELD_TYPE_CHOICES = (
        (GAME_TYPE, 'Game'),
        (TEAM_TYPE, 'Team'),
        (PLAYER_TYPE, 'Player'),
        (LEAGUE_TYPE, 'League'),
        (NEWS_TYPE, 'News'),
    )

    field_type = models.CharField(
        choices=FIELD_TYPE_CHOICES,
        blank=False,
        max_length=1
    )

    commented_id = models.IntegerField(
        blank=False
    )

    def __str__(self):
        return self.get_field_type_display() + ' : ' + str(self.commented_id)


class Comment(models.Model):
    field = models.ForeignKey(
        to=CommentField,
        on_delete=models.CASCADE,
        blank=False
    )
    profile = models.ForeignKey(
        to=espn_models.Profile,
        on_delete=models.CASCADE,
    )
    reply_to = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    text = models.CharField(
        max_length=2200,
        blank=False
    )

    def __str__(self):
        return self.profile.user.username + ' : ' + self.text


class CommentLike(models.Model):
    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        blank=True,
    )
    profile = models.OneToOneField(
        to=espn_models.Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.profile.user.username
