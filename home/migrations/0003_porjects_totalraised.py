# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191012_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Porjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('target', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='TotalRaised',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_raised', models.IntegerField(default=0)),
            ],
        ),
    ]
