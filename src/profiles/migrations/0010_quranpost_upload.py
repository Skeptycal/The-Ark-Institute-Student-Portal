# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20170809_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='quranpost',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
