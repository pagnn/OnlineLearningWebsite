# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-06 06:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_auto_20171206_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='categor',
            new_name='category',
        ),
    ]
