# Generated by Django 2.1.5 on 2019-01-25 11:50

import News.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=500)),
                ('news_text', models.TextField()),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(blank=True, max_length=256)),
                ('image', models.ImageField(upload_to=News.models.image_path)),
                ('image_description', models.CharField(blank=True, max_length=500)),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.News')),
            ],
        ),
        migrations.CreateModel(
            name='NewsResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_title', models.CharField(max_length=256)),
                ('resource_url', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.News')),
            ],
        ),
    ]
