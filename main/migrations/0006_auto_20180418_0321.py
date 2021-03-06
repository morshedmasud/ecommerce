# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-18 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180417_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='footer_address',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='footer_subscribe_info',
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='footer_address',
            field=models.TextField(default='Our address', help_text='Company address displayed on footer.'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='footer_subscribe_info',
            field=models.CharField(default='Pellentesque habitant morbi tristique senectus et netus \t\t\t\tet malesuada fames ac turpis egestas.', help_text='Text displayed above the subscription email field.', max_length=200),
        ),
    ]
