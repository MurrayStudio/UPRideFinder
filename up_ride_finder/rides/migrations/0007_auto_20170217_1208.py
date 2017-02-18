# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-17 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0006_auto_20170131_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='dest_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Friendly name of final destination'),
        ),
        migrations.AddField(
            model_name='ride',
            name='origin_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Friendly name of origin'),
        ),
    ]
