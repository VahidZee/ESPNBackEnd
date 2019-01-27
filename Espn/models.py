from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.html import format_html


@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()


# Create your models here.6


def profile_picture_path(instance, filename):
    return 'users/' + str(date.today()) + '/' + str(datetime.now().time()) + '-pp-' + filename.strip().replace(' ', '')


class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    profile_picture = models.ImageField(
        upload_to=profile_picture_path,
        blank=True
    )
    access_token = models.CharField(
        max_length=256,
        blank=True
    )

    def profile_image(self):
        res = '<img src="{}" width="50vw">'.format('http://127.0.0.1:8000/' + str(self.profile_picture.url))
        return format_html(res)


    def __str__(self):
        return self.user.username
