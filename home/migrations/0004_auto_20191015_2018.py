# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_porjects_totalraised'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Porjects',
            new_name='Projects',
        ),
    ]