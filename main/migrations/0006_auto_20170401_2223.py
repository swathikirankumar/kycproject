# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170401_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='applicant_score',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='reason_to_move',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='reason_to_reject',
        ),
        migrations.AddField(
            model_name='uploadidentification',
            name='applicant_score',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='uploadidentification',
            name='reason_to_move',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='uploadidentification',
            name='reason_to_reject',
            field=models.TextField(null=True),
        ),
    ]
