# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-06 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_image_back'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='featured_products',
            field=models.ManyToManyField(blank=True, to='shop.Product', verbose_name='Featured Products'),
        ),
    ]
