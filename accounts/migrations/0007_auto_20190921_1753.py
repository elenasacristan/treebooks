# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-21 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190921_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]