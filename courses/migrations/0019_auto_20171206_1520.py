# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-06 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('courses', '0018_course_secondary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='secondary',
        ),
        migrations.AddField(
            model_name='course',
            name='secondary',
            field=models.ManyToManyField(blank=True, null=True, related_name='secondary_category', to='categories.Category'),
        ),
    ]