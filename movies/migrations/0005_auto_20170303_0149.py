# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 01:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movietag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movietag',
            old_name='tagName',
            new_name='tag_name',
        ),
    ]