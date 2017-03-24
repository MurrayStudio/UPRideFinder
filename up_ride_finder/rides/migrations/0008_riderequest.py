# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 05:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0007_auto_20170217_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('AC', 'Accepted'), ('DE', 'Declined'), ('UN', 'Undecided')], default='UN', max_length=2)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ride', to='rides.Ride')),
            ],
        ),
    ]