# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-03 17:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='name_pic',
            field=models.CharField(default=datetime.datetime(2017, 8, 3, 17, 3, 2, 637972, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
