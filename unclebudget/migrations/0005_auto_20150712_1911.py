# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unclebudget', '0004_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='budgeted',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=9),
        ),
    ]
