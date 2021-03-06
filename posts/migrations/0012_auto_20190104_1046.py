# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-04 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20190103_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='theUserWhoIsFollowing',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='userWhoIsBeingFollowed',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='followerCount',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='followingCount',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(related_name='followed_by', to='posts.Profile'),
        ),
        migrations.DeleteModel(
            name='Follower',
        ),
    ]
