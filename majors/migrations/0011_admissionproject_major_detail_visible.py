# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majors', '0010_auto_20170830_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionproject',
            name='major_detail_visible',
            field=models.BooleanField(default=False, verbose_name='แสดงรายละเอียดสาขา'),
        ),
    ]