# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-14 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crypto',
            new_name='Dashconf',
        ),
    ]
