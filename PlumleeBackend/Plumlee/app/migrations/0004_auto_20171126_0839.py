# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 08:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171126_0838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='team_flagPic',
            new_name='team_flag_pic',
        ),
    ]
