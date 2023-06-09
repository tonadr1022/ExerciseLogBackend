# Generated by Django 4.2.1 on 2023-05-31 20:46

import api.models
import datetime
import datetimeutc.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_type', models.CharField(choices=[('Standard', 'Standard'), ('Long', 'Long'), ('Speed', 'Speed'), ('Recovery', 'Recovery')], max_length=8)),
                ('is_public', models.BooleanField(default=True)),
                ('created_at', datetimeutc.fields.DateTimeUTCField(auto_now_add=True)),
                ('name', models.CharField(default='Activity', max_length=100)),
                ('act_type', models.CharField(choices=[('Run', 'Run'), ('Bike', 'Bike'), ('Swim', 'Swim'), ('Elliptical', 'Elliptical'), ('Walk', 'Walk')], default='Run', max_length=30)),
                ('datetime_started', datetimeutc.fields.DateTimeUTCField(blank=True, default=django.utils.timezone.now, null=True)),
                ('duration', models.DurationField(blank=True, default=datetime.timedelta(0), null=True)),
                ('distance', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('pace', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, max_length=1000, null=True)),
                ('log_notes', models.TextField(blank=True, max_length=1000, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=True)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, max_length=1000, null=True)),
                ('distance_run', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('feels_like', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('wind_speed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_current_api', models.BooleanField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
    ]
