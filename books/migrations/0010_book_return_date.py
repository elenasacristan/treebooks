# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-05 01:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_remove_book_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='return_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
