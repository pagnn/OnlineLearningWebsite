# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-06 11:41
from __future__ import unicode_literals

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20171206_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', null=True, upload_to=courses.models.handle_upload, width_field='image_width'),
        ),
        migrations.AddField(
            model_name='course',
            name='image_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='image_width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
