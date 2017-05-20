# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vahay', '0004_auto_20170518_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.CharField(max_length=1000)),
                ('vahay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vahay.Vahay')),
            ],
        ),
    ]