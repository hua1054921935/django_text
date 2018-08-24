#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:python
# datetime:18-8-7 上午10:54
# software: PyCharm
from rest_framework import serializers
from .models import Machines
class Machinesserializers(serializers.Serializer):
    # node_id = models.IntegerField('节点ID')
    machine_id = serializers.BigIntegerField('机器ID', primary_key=True)
    # name = models.CharField('名称', max_length=128)
    status = serializers.CharField('状态', max_length=32)
    # vcpu_num = models.IntegerField('VCPU数量')
    cpu_usage = serializers.DecimalField('CPU使用率', max_digits=4, decimal_places=2)
    mem_usage = serializers.DecimalField('内存使用率', max_digits=4, decimal_places=2)
    disk_usage = serializers.DecimalField('硬盘使用率', max_digits=4, decimal_places=2)
    # machine_ip = models.GenericIPAddressField(
    #     '服务器IP', max_length=32, db_index=True)
    readio_usage = serializers.DecimalField('读取速率', max_digits=4, decimal_places=2)
    writeio_usage = serializers.DecimalField('写入速率', max_digits=4, decimal_places=2)

    created_time = serializers.DateTimeField('创建时间', auto_now_add=True)
