# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('unclebudget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='name',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 7, 12, 1, 2, 42, 341821, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='comment',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 7, 12, 1, 2, 49, 29676, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
