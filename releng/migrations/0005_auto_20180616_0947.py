# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-16 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releng', '0004_auto_20170524_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='architecture',
        ),
        migrations.RemoveField(
            model_name='test',
            name='boot_type',
        ),
        migrations.RemoveField(
            model_name='test',
            name='bootloader',
        ),
        migrations.RemoveField(
            model_name='test',
            name='clock_choice',
        ),
        migrations.RemoveField(
            model_name='test',
            name='filesystem',
        ),
        migrations.RemoveField(
            model_name='test',
            name='hardware_type',
        ),
        migrations.RemoveField(
            model_name='test',
            name='install_type',
        ),
        migrations.RemoveField(
            model_name='test',
            name='iso',
        ),
        migrations.RemoveField(
            model_name='test',
            name='iso_type',
        ),
        migrations.RemoveField(
            model_name='test',
            name='modules',
        ),
        migrations.RemoveField(
            model_name='test',
            name='rollback_filesystem',
        ),
        migrations.RemoveField(
            model_name='test',
            name='rollback_modules',
        ),
        migrations.RemoveField(
            model_name='test',
            name='source',
        ),
        migrations.DeleteModel(
            name='Architecture',
        ),
        migrations.DeleteModel(
            name='Bootloader',
        ),
        migrations.DeleteModel(
            name='BootType',
        ),
        migrations.DeleteModel(
            name='ClockChoice',
        ),
        migrations.DeleteModel(
            name='Filesystem',
        ),
        migrations.DeleteModel(
            name='HardwareType',
        ),
        migrations.DeleteModel(
            name='InstallType',
        ),
        migrations.DeleteModel(
            name='Iso',
        ),
        migrations.DeleteModel(
            name='IsoType',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
