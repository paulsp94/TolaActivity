# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0002_auto_20170707_0539'),
        ('workflow', '0010_auto_20170727_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflowlevel2',
            name='indicators',
            field=models.ManyToManyField(blank=True, to='indicators.Indicator'),
        ),
    ]