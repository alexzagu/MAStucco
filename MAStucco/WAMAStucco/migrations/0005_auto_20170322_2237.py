# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-23 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WAMAStucco', '0004_auto_20170322_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, default='NA', max_length=2),
        ),
    ]
