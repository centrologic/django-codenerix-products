# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-17 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0035_productfinal_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfinal',
            name='code',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Code'),
        ),
        migrations.AddField(
            model_name='productfinal',
            name='price_base_local',
            field=models.FloatField(blank=True, null=True, verbose_name='Price base'),
        ),
    ]
