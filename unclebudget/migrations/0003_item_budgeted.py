# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unclebudget', '0002_auto_20150712_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='budgeted',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
