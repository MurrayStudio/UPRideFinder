# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-01 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='trip_id',
        ),
        migrations.AlterField(
            model_name='ride',
            name='destination',
            field=models.CharField(max_length=5, verbose_name='ZIP code of final destination'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='origin',
            field=models.CharField(max_length=5, verbose_name='ZIP code of origin'),
        ),
    ]
