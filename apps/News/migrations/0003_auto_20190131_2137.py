# Generated by Django 2.1.5 on 2019-01-31 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20190131_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstag',
            name='news',
            field=models.ManyToManyField(blank=True, to='News.News'),
        ),
    ]
