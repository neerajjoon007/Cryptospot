# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-19 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20181026_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='airdrop',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]
