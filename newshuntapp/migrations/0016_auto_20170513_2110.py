# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newshuntapp', '0015_auto_20170513_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='dislikes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]
