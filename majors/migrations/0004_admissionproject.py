# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majors', '0003_admissionround'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('short_title', models.CharField(max_length=200)),
                ('general_conditions', models.TextField(blank=True)),
                ('column_descriptions', models.TextField(blank=True)),
                ('admission_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='majors.AdmissionRound')),
                ('campus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='majors.Campus')),
            ],
        ),
    ]
