# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 07:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflow', '0015_auto_20170814_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalIssueRegister',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=135, null=True)),
                ('impact', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
                ('cause', models.CharField(blank=True, max_length=255, null=True)),
                ('date_opened', models.DateTimeField(blank=True, null=True)),
                ('date_resolved', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('assigned', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.TolaUser')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical issue register',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRiskRegister',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=135, null=True)),
                ('impact', models.CharField(blank=True, max_length=255, null=True)),
                ('likelihood', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('contingency_plan', models.CharField(blank=True, max_length=255, null=True)),
                ('mitigation_plan', models.CharField(blank=True, max_length=255, null=True)),
                ('post_mitigation_status', models.CharField(blank=True, max_length=255, null=True)),
                ('action_by', models.DateTimeField(blank=True, null=True)),
                ('action_when', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical risk register',
            },
        ),
        migrations.CreateModel(
            name='IssueRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=135, null=True)),
                ('impact', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
                ('cause', models.CharField(blank=True, max_length=255, null=True)),
                ('date_opened', models.DateTimeField(blank=True, null=True)),
                ('date_resolved', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.TolaUser')),
            ],
            options={
                'ordering': ('type', 'name'),
            },
        ),
        migrations.CreateModel(
            name='RiskRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=135, null=True)),
                ('impact', models.CharField(blank=True, max_length=255, null=True)),
                ('likelihood', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('contingency_plan', models.CharField(blank=True, max_length=255, null=True)),
                ('mitigation_plan', models.CharField(blank=True, max_length=255, null=True)),
                ('post_mitigation_status', models.CharField(blank=True, max_length=255, null=True)),
                ('action_by', models.DateTimeField(blank=True, null=True)),
                ('action_when', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('type', 'name'),
            },
        ),
    ]