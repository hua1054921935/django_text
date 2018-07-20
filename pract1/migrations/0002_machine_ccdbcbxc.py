# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pract1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine_ccdbcbxc',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('trans_packetsssss', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Machine_ccdbcbxc',
                'verbose_name': 'Machine_ccdbcbxc',
            },
        ),
    ]
