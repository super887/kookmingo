# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kookmingo', '0008_auto_20170314_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='DormitoryD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cafe_name', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('menu', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='DormitoryN',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cafe_name', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('menu', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Hanul',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cafe_name', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('menu', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Smell',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cafe_name', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('menu', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cafe_name', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('menu', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cafe_name', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('menu', models.TextField(max_length=2000)),
            ],
        ),
    ]
