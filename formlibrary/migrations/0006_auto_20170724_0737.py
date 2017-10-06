# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 14:37
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formlibrary', '0005_auto_20170711_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customform',
            name='fields',
        ),
        migrations.AddField(
            model_name='customform',
            name='fields',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]