# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-28 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20180922_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='item_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='itempic',
            field=models.ImageField(blank=True, null=True, upload_to='Banners'),
        ),
    ]
