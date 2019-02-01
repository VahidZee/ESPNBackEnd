# Generated by Django 2.1.5 on 2019-02-01 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Espn', '0001_initial'),
        ('Comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentlike',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Espn.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Comment.CommentField'),
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Espn.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Comment.Comment'),
        ),
    ]
