# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newshuntapp', '0018_auto_20170513_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newshuntapp.Category'),
        ),
    ]
