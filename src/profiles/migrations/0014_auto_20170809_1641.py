# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 20:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20170809_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qurancomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
