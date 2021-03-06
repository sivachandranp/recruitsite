# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-10 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('first_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.TextField()),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.IntegerField(blank=True, max_length=20, null=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True)),
                ('dob', models.CharField(max_length=100, verbose_name='Date of Birth')),
                ('mobile_number', models.CharField(max_length=60, verbose_name='Personal Telephone')),
                ('home_number', models.CharField(max_length=60, verbose_name='Home Telephone')),
                ('email', models.EmailField(max_length=254)),
                ('position_sought', models.CharField(blank=True, max_length=100, null=True)),
                ('available_date', models.CharField(blank=True, max_length=60, null=True)),
                ('currently_employed', models.NullBooleanField(max_length=10)),
                ('pay_range_expectation', models.CharField(blank=True, max_length=20, null=True)),
                ('latest_qualification', models.CharField(blank=True, max_length=50, null=True)),
                ('year_passed_out', models.IntegerField()),
                ('total_experience', models.IntegerField(blank=True, max_length=5, null=True)),
                ('previous_company', models.CharField(blank=True, max_length=250, null=True)),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'application_form',
            },
        ),
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('app_id', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.CharField(blank=True, max_length=75, null=True)),
            ],
            options={
                'db_table': 'application_status',
            },
        ),
    ]
