from django.db import models

# Create your models here.
class Machines(models.Model):
    # node_id = models.IntegerField('节点ID')
    machine_id = models.BigIntegerField('机器ID', primary_key=True)
    # name = models.CharField('名称', max_length=128)
    status = models.CharField('状态', max_length=32)
    # vcpu_num = models.IntegerField('VCPU数量')
    cpu_usage = models.DecimalField('CPU使用率', max_digits=4, decimal_places=2)
    mem_usage = models.DecimalField('内存使用率', max_digits=4, decimal_places=2)
    disk_usage = models.DecimalField('硬盘使用率',max_digits=4, decimal_places=2)
    # machine_ip = models.GenericIPAddressField(
    #     '服务器IP', max_length=32, db_index=True)
    readio_usage = models.DecimalField('读取速率', max_digits=4, decimal_places=2)
    writeio_usage = models.DecimalField('写入速率', max_digits=4, decimal_places=2)

    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = "Machines"
        verbose_name_plural = "Machines"

    # def __unicode__(self):
    #     return self.name
class Machineinterface(models.Model):
    # node_id = models.IntegerField('节点ID')
    machine_id = models.BigIntegerField('机器ID', primary_key=True)
    # name = models.CharField('名称', max_length=128)
    Interface_id = models.IntegerField('网卡ID')
    record_time = models.DateTimeField(auto_now=True)
    recv_byte = models.BigIntegerField(blank=True, null=True)
    recv_packets = models.IntegerField(blank=True, null=True)
    trans_byte = models.BigIntegerField(blank=True, null=True)
    trans_packets = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Machineinterface"
        verbose_name_plural = "Machineinterface"
class Machineinterfaces(models.Model):
    # node_id = models.IntegerField('节点ID')
    machine_id = models.BigIntegerField('机器ID', primary_key=True)
    # name = models.CharField('名称', max_length=128)
    Interface_id = models.IntegerField('网卡ID')
    record_time = models.DateTimeField(auto_now=True)
    recv_byte = models.BigIntegerField(blank=True, null=True)
    recv_packets = models.IntegerField(blank=True, null=True)
    trans_byte = models.BigIntegerField(blank=True, null=True)
    trans_packets = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Machineinterfaces"
        verbose_name_plural = "Machineinterfaces"
class Test01(models.Model):
    ecord_time = models.DateTimeField(auto_now=True)
    recv_byte = models.BigIntegerField(blank=True, null=True)
    recv_packets = models.IntegerField(blank=True, null=True)
    trans_byte = models.BigIntegerField(blank=True, null=True)
    trans_packets = models.IntegerField(blank=True, null=True)
    class Meta:
        verbose_name = "Test01"
        verbose_name_plural = "Test01"
class Machine_b(models.Model):
    # node_id = models.IntegerField('节点ID')
    machine_id = models.BigIntegerField('机器ID', primary_key=True)
    # name = models.CharField('名称', max_length=128)
    Interface_id = models.IntegerField('网卡ID')
    record_time = models.DateTimeField(auto_now=True)
    recv_byte = models.BigIntegerField(blank=True, null=True)
    recv_packets = models.IntegerField(blank=True, null=True)
    trans_byte = models.BigIntegerField(blank=True, null=True)
    trans_packets = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Machine_b"
        verbose_name_plural = "Machine_b"
class Machine_bx(models.Model):
    # node_id = models.IntegerField('节点ID')

    trans_byte = models.BigIntegerField(blank=True, null=True)
    trans_packets = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Machine_bx"
        verbose_name_plural = "Machine_bx"
class Machine_cb(models.Model):
    # node_id = models.IntegerField('节点ID')

    trans_packets = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Machine_cb"
        verbose_name_plural = "Machine_cb"
class Machine_cbx(models.Model):
    # node_id = models.IntegerField('节点ID')
    trans_packetss = models.IntegerField(blank=True, null=True)
    trans_packets = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Machine_cbx"
        verbose_name_plural = "Machine_cbx"
class Machine_cbxc(models.Model):
    # node_id = models.IntegerField('节点ID')
    trans_packetss = models.IntegerField(blank=True, null=True)
    trans_packets = models.IntegerField(blank=True, null=True)
    trans_packetsss = models.IntegerField(blank=True, null=True)
    trans_packetsssss = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Machine_cbxc"
        verbose_name_plural = "Machine_cbxc"
class Machine_bcbxc(models.Model):
    # node_id = models.IntegerField('节点ID')

    trans_packetsssss = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Machine_bcbxc"
        verbose_name_plural = "Machine_bcbxc"


class Machine_dbcbxc(models.Model):
    # node_id = models.IntegerField('节点ID')

    trans_packetsssss = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Machine_dbcbxc"
        verbose_name_plural = "Machine_dbcbxc"

class Machine_ccdbcbxc(models.Model):
    # node_id = models.IntegerField('节点ID')

    trans_packetsssss = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Machine_ccdbcbxc"
        verbose_name_plural = "Machine_ccdbcbxc"

class Django_asss(models.Model):
    pass

class Django_asss(models.Model):
    pass