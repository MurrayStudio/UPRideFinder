# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-01 01:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import up_ride_finder.rides.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0004_auto_20170201_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='available_seats',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Maximum number of passengers'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='origin',
            field=models.CharField(max_length=5, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='ZIP code of origin'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='when',
            field=models.DateTimeField(validators=[up_ride_finder.rides.validators.future_date], verbose_name='Approximate departure date and time'),
        ),
    ]
