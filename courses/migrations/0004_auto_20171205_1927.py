# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-05 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='description',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
