# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unclebudget', '0005_auto_20150712_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='singleton',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='budgeted',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]