# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2020-03-23 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_creview_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='creview',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='preview',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
