# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-24 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(blank=True, default='images/default_profile.png', upload_to='images'),
        ),
    ]
