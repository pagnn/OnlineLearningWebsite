# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-06 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20171206_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
