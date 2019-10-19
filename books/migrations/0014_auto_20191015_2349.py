# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 22:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20191015_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='current_reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]