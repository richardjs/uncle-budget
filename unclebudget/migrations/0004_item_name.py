# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unclebudget', '0003_item_budgeted'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
    ]
