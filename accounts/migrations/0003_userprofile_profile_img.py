# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-21 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userprofile_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(default='default_profile.png', upload_to='images'),
        ),
    ]