# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-23 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=12345678, max_length=255),
            preserve_default=False,
        ),
    ]
