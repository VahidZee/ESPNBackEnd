# General Imports
from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

# Model Imports
from apps.Espn import models as espn_models
from apps.News import models as news_models


# Local Imports

# Comment Fields for news
@receiver(post_save, sender=news_models.News)
def create_news_dependencies(sender, created, instance, **kwargs):
    if created:
        comment_field = CommentField()
        comment_field.commented_id = instance.id
        comment_field.field_type = 'N'
        comment_field.save()


@receiver(post_delete, sender=news_models.News)
def remove_news_dependencies(sender, instance, **kwargs):
    comment_field = CommentField.objects.get(
        commented_id=instance.id,
        field_type='N',
    )
    comment_field.delete()


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

    uploaded_at = models.DateTimeField(
        auto_now=True,
    )

    def likes_count(self):
        return CommentLike.objects.filter(comment=self).count()

    def comment_json_dict(self, profile=None):
        is_liked = False,
        if profile:
            try:
                comment_like = CommentLike.objects.get(
                    comment=self,
                    profile=profile,
                )
                is_liked = True,
            except Exception:
                pass
        replys_objects = Comment.objects.filter(reply_to=self)
        replys = [comment.comment_json_dict() for comment in replys_objects]
        return {
            'id': self.id,
            'userInfo': self.profile.info_json(),
            'publishDate': self.uploaded_at.isoformat(),
            'text': self.text,
            'likesCount': self.likes_count(),
            'liked': bool(is_liked[0]),
            'replies': replys
        }

    def __str__(self):
        return self.profile.user.username + ' : ' + self.text


class CommentLike(models.Model):
    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        blank=True,
    )
    profile = models.ForeignKey(
        to=espn_models.Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.profile.user.username
