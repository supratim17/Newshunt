# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newshuntapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newshuntapp.Role'),
        ),
    ]
