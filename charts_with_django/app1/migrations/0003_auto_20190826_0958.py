# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-08-26 09:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20190826_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='Class',
            new_name='AClass',
        ),
    ]
