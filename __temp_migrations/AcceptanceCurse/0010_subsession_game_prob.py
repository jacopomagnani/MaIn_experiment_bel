# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-17 06:44
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AcceptanceCurse', '0009_auto_20180917_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsession',
            name='game_prob',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
