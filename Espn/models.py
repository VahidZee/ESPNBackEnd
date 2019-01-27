from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime


# Create your models here.


def profile_picture_path(instance, filename):
    return 'users/' + str(date.today()) + '/' + str(datetime.now().time()) + '-pp-' + filename.strip().replace(' ', '')


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=profile_picture_path,blank=True)
    access_token = models.CharField(max_length=256, blank=True)
