# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 03:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kookmingo', '0009_dormitoryd_dormitoryn_hanul_smell_staff_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DormitoryD',
        ),
        migrations.DeleteModel(
            name='DormitoryN',
        ),
        migrations.DeleteModel(
            name='Hanul',
        ),
        migrations.DeleteModel(
            name='Smell',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]