# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-06 01:16
from __future__ import unicode_literals

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20171206_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='order',
            field=courses.fields.PositionField(default=-1),
        ),
    ]
