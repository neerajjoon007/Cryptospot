# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-28 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_remove_dashconf_market_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dashconf',
            new_name='Dashconfig',
        ),
    ]
