# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 13:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=200)),
                ('last', models.CharField(max_length=200)),
                ('picture', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('User_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('videoid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('like', models.BigIntegerField(default=0)),
                ('dislike', models.BigIntegerField(default=0)),
                ('viewCount', models.BigIntegerField(default=0)),
                ('category', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video_url', models.TextField(default='null')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'video',
            },
        ),
    ]