# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-08 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
