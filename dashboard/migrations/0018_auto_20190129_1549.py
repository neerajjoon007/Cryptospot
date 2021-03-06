# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-29 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_dashconfig_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashconfig',
            name='logo',
            field=models.ImageField(blank=True, default='Banners/logo_orange.png', null=True, upload_to='Banners'),
        ),
        migrations.AlterField(
            model_name='dashconfig',
            name='sidebar_image',
            field=models.ImageField(blank=True, default='Banners/bitcoin-lighting.jpg', null=True, upload_to='Banners'),
        ),
    ]
