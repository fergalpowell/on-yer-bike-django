# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_bikestation_no_stands'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikestation',
            name='no_stands',
            field=models.CharField(max_length=25),
        ),
    ]
