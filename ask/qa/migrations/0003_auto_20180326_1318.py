# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 13:18
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20180325_2311'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='question',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
