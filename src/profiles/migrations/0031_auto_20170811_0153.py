# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-11 05:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0030_auto_20170811_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quranexam',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quran_exam_scores', to=settings.AUTH_USER_MODEL),
        ),
    ]
