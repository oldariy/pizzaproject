# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-11 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashop', '0017_auto_20171210_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=150, verbose_name='Адес'),
        ),
    ]