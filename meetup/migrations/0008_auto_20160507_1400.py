# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-07 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0007_auto_20160507_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='lat',
            field=models.FloatField(blank=True, null=True, verbose_name='위도'),
        ),
        migrations.AddField(
            model_name='meetup',
            name='location',
            field=models.CharField(default='google', max_length=50, verbose_name='장소 이름'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='lon',
            field=models.FloatField(blank=True, null=True, verbose_name='경도'),
        ),
    ]