# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 03:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.IntegerField(verbose_name='ZIP code of final destination')),
                ('origin', models.IntegerField(verbose_name='ZIP code of origin')),
                ('available_seats', models.IntegerField(verbose_name='Maximum number of passengers')),
                ('cost', models.CharField(max_length=255, verbose_name='Approx. cost the driver expects riders to pay.')),
                ('when', models.DateTimeField(verbose_name='Approximate departure date and time')),
                ('trip_summary', models.CharField(max_length=255, verbose_name='Summary of the trip')),
                ('trip_id', models.PositiveIntegerField(verbose_name='Trip ID')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL)),
                ('riders', models.ManyToManyField(related_name='riders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]