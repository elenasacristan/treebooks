# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-21 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190921_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(default='default_profile.png', upload_to='images'),
        ),
    ]