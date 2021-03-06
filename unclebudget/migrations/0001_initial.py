# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 00:03
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
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('budgeted', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('income', models.BooleanField(default=False)),
                ('singleton', models.BooleanField(default=False)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unclebudget.Budget')),
                ('transfer_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfer_set', to='unclebudget.Budget')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('comment', models.CharField(max_length=200)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unclebudget.Item')),
            ],
        ),
    ]
