# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-10 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20191010_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewbook',
            name='score',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]