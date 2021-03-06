# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20170807_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image_full',
        ),
        migrations.AddField(
            model_name='post',
            name='image_display',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
