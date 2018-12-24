# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-14 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Propic',
            field=models.ImageField(blank=True, null=True, upload_to=b'profile_pics/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
