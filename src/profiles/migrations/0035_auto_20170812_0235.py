# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-12 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0034_auto_20170812_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='unseen_islamic_studies_exams',
            field=models.ManyToManyField(blank=True, related_name='unseen_islamic_studies_exams', to='profiles.IslamicStudiesExam'),
        ),
        migrations.AddField(
            model_name='profile',
            name='unseen_quran_exams',
            field=models.ManyToManyField(blank=True, related_name='unseen_quran_exams', to='profiles.QuranExam'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unread_islamic_studies_comments',
            field=models.ManyToManyField(blank=True, related_name='unread_islamic_studies_comments', to='profiles.IslamicStudiesComment'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unread_islamic_studies_posts',
            field=models.ManyToManyField(blank=True, related_name='unread_islamic_studies_posts', to='profiles.IslamicStudiesPost'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unread_quran_comments',
            field=models.ManyToManyField(blank=True, related_name='unread_quran_comments', to='profiles.QuranComment'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unread_quran_posts',
            field=models.ManyToManyField(blank=True, related_name='unread_quran_posts', to='profiles.QuranPost'),
        ),
    ]
