# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine_b',
            fields=[
                ('machine_id', models.BigIntegerField(serialize=False, verbose_name='机器ID', primary_key=True)),
                ('Interface_id', models.IntegerField(verbose_name='网卡ID')),
                ('record_time', models.DateTimeField(auto_now=True)),
                ('recv_byte', models.BigIntegerField(blank=True, null=True)),
                ('recv_packets', models.IntegerField(blank=True, null=True)),
                ('trans_byte', models.BigIntegerField(blank=True, null=True)),
                ('trans_packets', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Machine_b',
                'verbose_name_plural': 'Machine_b',
            },
        ),
        migrations.CreateModel(
            name='Machine_bcbxc',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('trans_packetsssss', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Machine_bcbxc',
                'verbose_name_plural': 'Machine_bcbxc',
            },
        ),
        migrations.CreateModel(
            name='Machine_bx',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('trans_byte', models.BigIntegerField(blank=True, null=True)),
                ('trans_packets', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Machine_bx',
                'verbose_name_plural': 'Machine_bx',
            },
        ),
        migrations.CreateModel(
            name='Machine_cb',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('trans_packets', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Machine_cb',
                'verbose_name_plural': 'Machine_cb',
            },
        ),
        migrations.CreateModel(
            name='Machine_cbx',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('trans_packetss', models.IntegerField(blank=True, null=True)),
                ('trans_packets', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Machine_cbx',
                'verbose_name_plural': 'Machine_cbx',
            },
        ),
        migrations.CreateModel(
            name='Machine_cbxc',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('trans_packetss', models.IntegerField(blank=True, null=True)),
                ('trans_packets', models.IntegerField(blank=True, null=True)),
                ('trans_packetsss', models.IntegerField(blank=True, null=True)),
                ('trans_packetsssss', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Machine_cbxc',
                'verbose_name_plural': 'Machine_cbxc',
            },
        ),
        migrations.CreateModel(
            name='Machine_dbcbxc',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('trans_packetsssss', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Machine_dbcbxc',
                'verbose_name_plural': 'Machine_dbcbxc',
            },
        ),
        migrations.CreateModel(
            name='Machineinterface',
            fields=[
                ('machine_id', models.BigIntegerField(serialize=False, verbose_name='机器ID', primary_key=True)),
                ('Interface_id', models.IntegerField(verbose_name='网卡ID')),
                ('record_time', models.DateTimeField(auto_now=True)),
                ('recv_byte', models.BigIntegerField(blank=True, null=True)),
                ('recv_packets', models.IntegerField(blank=True, null=True)),
                ('trans_byte', models.BigIntegerField(blank=True, null=True)),
                ('trans_packets', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Machineinterface',
                'verbose_name_plural': 'Machineinterface',
            },
        ),
        migrations.CreateModel(
            name='Machineinterfaces',
            fields=[
                ('machine_id', models.BigIntegerField(serialize=False, verbose_name='机器ID', primary_key=True)),
                ('Interface_id', models.IntegerField(verbose_name='网卡ID')),
                ('record_time', models.DateTimeField(auto_now=True)),
                ('recv_byte', models.BigIntegerField(blank=True, null=True)),
                ('recv_packets', models.IntegerField(blank=True, null=True)),
                ('trans_byte', models.BigIntegerField(blank=True, null=True)),
                ('trans_packets', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Machineinterfaces',
                'verbose_name_plural': 'Machineinterfaces',
            },
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('machine_id', models.BigIntegerField(serialize=False, verbose_name='机器ID', primary_key=True)),
                ('status', models.CharField(verbose_name='状态', max_length=32)),
                ('cpu_usage', models.DecimalField(verbose_name='CPU使用率', max_digits=4, decimal_places=2)),
                ('mem_usage', models.DecimalField(verbose_name='内存使用率', max_digits=4, decimal_places=2)),
                ('disk_usage', models.DecimalField(verbose_name='硬盘使用率', max_digits=4, decimal_places=2)),
                ('readio_usage', models.DecimalField(verbose_name='读取速率', max_digits=4, decimal_places=2)),
                ('writeio_usage', models.DecimalField(verbose_name='写入速率', max_digits=4, decimal_places=2)),
                ('created_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Machines',
                'verbose_name_plural': 'Machines',
            },
        ),
        migrations.CreateModel(
            name='Test01',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('ecord_time', models.DateTimeField(auto_now=True)),
                ('recv_byte', models.BigIntegerField(blank=True, null=True)),
                ('recv_packets', models.IntegerField(blank=True, null=True)),
                ('trans_byte', models.BigIntegerField(blank=True, null=True)),
                ('trans_packets', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Test01',
                'verbose_name_plural': 'Test01',
            },
        ),
    ]
