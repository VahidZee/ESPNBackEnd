# Generated by Django 2.1.5 on 2019-01-31 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Espn', '0004_profile_forget_password_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
