# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-20 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Book'),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.Order'),
        ),
    ]