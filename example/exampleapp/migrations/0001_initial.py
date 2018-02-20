# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-23 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import username_tools.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HypotheticalUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', username_tools.fields.UsernameModelField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='username')),
            ],
        ),
    ]
