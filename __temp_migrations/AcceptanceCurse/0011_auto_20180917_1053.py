# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-17 06:53
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AcceptanceCurse', '0010_subsession_game_prob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='choice',
            field=otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']]),
        ),
    ]