# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-06 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20171206_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='secondary',
            field=models.ManyToManyField(blank=True, related_name='secondary_category', to='categories.Category'),
        ),
    ]
