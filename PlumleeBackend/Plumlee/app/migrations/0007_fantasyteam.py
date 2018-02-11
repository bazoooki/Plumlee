# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_player_points_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='FantasyTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=100)),
                ('team_total_score', models.CharField(blank=True, max_length=100)),
                ('team_id', models.IntegerField(blank=True)),
                ('allowed_subs', models.FloatField(blank=True, default=0)),
                ('subs_made', models.FloatField(blank=True, default=0)),
                ('remaining_budget', models.FloatField(blank=True, default=0)),
                ('coach_name', models.CharField(blank=True, max_length=100)),
                ('players', models.ManyToManyField(related_name='players', to='app.Player')),
            ],
        ),
    ]
