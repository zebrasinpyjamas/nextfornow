# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfn_contests', '0006_auto_20151214_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='is_winner',
            field=models.BooleanField(default=False, verbose_name='Yes!'),
        ),
    ]