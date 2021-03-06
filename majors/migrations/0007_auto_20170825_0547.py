# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majors', '0006_auto_20170824_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admissionproject',
            name='admission_round',
        ),
        migrations.AddField(
            model_name='admissionproject',
            name='admission_rounds',
            field=models.ManyToManyField(to='majors.AdmissionRound'),
        ),
        migrations.AlterField(
            model_name='admissionproject',
            name='descriptions',
            field=models.TextField(blank=True, verbose_name='รายละเอียดโครงการ'),
        ),
        migrations.AlterField(
            model_name='admissionproject',
            name='short_descriptions',
            field=models.CharField(blank=True, max_length=400, verbose_name='รายละเอียดโครงการ (สั้น) แสดงในหน้าแรก'),
        ),
        migrations.AlterField(
            model_name='admissionround',
            name='admission_dates',
            field=models.CharField(blank=True, max_length=200, verbose_name='กำหนดการ'),
        ),
        migrations.AlterField(
            model_name='admissionround',
            name='short_descriptions',
            field=models.CharField(blank=True, max_length=400, verbose_name='รายละเอียดสั้น ๆ (แสดงในหน้าแรก)'),
        ),
    ]
