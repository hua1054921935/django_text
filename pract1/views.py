from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django.db import connection
from django.core.cache import cache
import time
import threading
import os
import json
import datetime


# Create your views here.
class Meyhod(View):
    def get(self,request):
        n = 200
        pos = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        r = 4
        d = 1
        count = 0
        node_id = 1
        nodes_list2 = []
        dict1 = {}

        try:
            for k in range(1, 18):
                y = r * k
                if k == 1:
                    for i in range(1, n):
                        for j in range(1, n):
                            for s in range(len(pos)):
                                nodes_dict = {}
                                nodes_dict['site'] = [i * pos[s][0], y, j * pos[s][1]]
                                # nodes_dict['node_type'] = 'host'
                                dict1[node_id] = nodes_dict
                                nodes_list2.append([i * pos[s][0], y, j * pos[s][1]])

                                count += 1
                                node_id += 1
                                # top_json['host'] = nodes_list1

                else:

                    yb = r * (k - 1)
                    for i in range(1, n):
                        for j in range(1, n):
                            for s in range(len(pos)):
                                nodes_list2.append([pos[s][0] * (d * (i - 0.5) + 0.5), y,
                                                    (d * (j - 0.5) + 0.5) * pos[s][1]])
                                nodes_dict = {}
                                nodes_dict['site'] = [pos[s][0] * (d * (i - 0.5) + 0.5), y,
                                                      (d * (j - 0.5) + 0.5) * pos[s][1]]
                                nodes_dict['line'] = [
                                    nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5) - 0.5, y - 4,
                                                       (d * (j - 0.5) + 0.5) * pos[s][1] - 0.5]) + 1,
                                    nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5) - 0.5, y - 4,
                                                       (d * (j - 0.5) + 0.5) * pos[s][1] + 0.5]) + 1,
                                    nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5) + 0.5, y - 4,
                                                       (d * (j - 0.5) + 0.5) * pos[s][1] - 0.5]) + 1,
                                    nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5) + 0.5, y - 4,
                                                       (d * (j - 0.5) + 0.5) * pos[s][1] + 0.5]) + 1]
                                # nodes_dict['node_type'] = 'switch'
                                dict1[node_id] = nodes_dict

                                count += 1
                                node_id += 1

                n = int(n * 0.5)
                d = d * 2
        except Exception as e:
            pass
        case_path = os.path.join(settings.NFS_ROOT, 'CaseDefinitions', '20160802145159627416')
        with open(case_path + '/topology.json', 'wb') as f:
            json.dump(dict1, f)
        os.chmod(case_path + '/topology.json', stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)

        return count


    def post(self, request):
        pass
class Meyhod1(View):
    def get(self, request):
        res=cache.get('res')
        if res is None:
            time.sleep(1)
            res='{"case": {"out": [{"name": "\u5355\u72ec\u4f7f\u7528", "value": 873}, {"name": "\u6559\u5b66\u6f14\u793a", "value": 1469}, {"name": "\u5f00\u653e\u5b9e\u9a8c", "value": 210}, {"name": "\u7ec3\u4e60\u5b9e\u9a8c", "value": 30}, {"name": "\u57f9\u8bad\u8003\u8bd5", "value": 40}, {"name": "\u6bd4\u6b66\u7ade\u8d5b", "value": 110}, {"name": "\u5de5\u5177\u5b9e\u9a8c", "value": 44}, {"name": "\u6311\u6218\u5b9e\u4f8b", "value": 811}, {"name": "\u4e3b\u673a\u7ba1\u7406", "value": 5}], "in": [{"name": "\u521d\u59cb\u5b9a\u4e49", "value": 3498}, {"name": "\u5b8c\u6210\u90e8\u7f72", "value": 11}, {"name": "\u8fd0\u884c\u72b6\u6001", "value": 16}, {"name": "\u7ed3\u675f\u72b6\u6001", "value": 67}]}, "weapon": {"in": [{"name": "linux", "value": 1}, {"name": "mac", "value": 2}, {"name": "windows", "value": 11}], "out": [{"name": "\u653b\u51fb\u7c7b", "value": 3}, {"name": "\u626b\u63cf\u7c7b", "value": 5}, {"name": "\u6728\u9a6c\u578b", "value": 1}, {"name": "\u75c5\u6bd2\u578b", "value": 2}, {"name": "\u7834\u574f\u578b", "value": 1}, {"name": "\u6df7\u5408\u578b", "value": 1}, {"name": "\u667a\u80fd\u578b", "value": 1}]}, "host": {"out": [{"name": "\u521d\u59cb\u5b9a\u4e49", "value": 5}], "in": [{"name": "linux", "value": 1}, {"name": "mac", "value": 1}, {"name": "windows", "value": 3}]}, "template": {"in": [{"name": "linux", "value": 31}, {"name": "mac", "value": 1}, {"name": "windows", "value": 41}]}, "device": {"in": [{"name": "\u6a21\u62df\u670d\u52a1\u5668", "value": 3}, {"name": "\u5b9e\u7269\u670d\u52a1\u5668", "value": 1}, {"name": "\u4eff\u771f\u670d\u52a1\u5668(KVM)", "value": 57}, {"name": "\u7cfb\u7edf\u8bbe\u5907", "value": 2}]}, "nodes": {"in": [{"name": "con", "value": 9}, {"name": "emu", "value": 18977}, {"name": "mms", "value": 183390}, {"name": "ope", "value": 16}, {"name": "rea", "value": 67}, {"name": "real", "value": 58}, {"name": "sim", "value": 680825}, {"name": "xen", "value": 3}], "out": [{"name": "d", "value": 86}, {"name": "f", "value": 478}, {"name": "h", "value": 842702}, {"name": "p", "value": 68}, {"name": "r", "value": 7699}, {"name": "s", "value": 31314}, {"name": "v", "value": 998}]}, "software": {"in": [{"name": "linux", "value": 3}, {"name": "mac", "value": 1}, {"name": "windows", "value": 23}], "out": [{"name": "\u7cfb\u7edf\u7c7b", "value": 11}, {"name": "\u529e\u516c\u7c7b", "value": 7}, {"name": "\u670d\u52a1\u7c7b", "value": 6}, {"name": "\u5b58\u50a8\u7c7b", "value": 3}]}}'
            cache.set('res',res,30)
            cache.set('ress','hello',30)
        else:
            res=cache.get('res')



        return HttpResponse(res)

        # return render(request,'a.html')

    def post(self, request):
        pass


def get_data(r,pos,):
    pass


def get_case_data(request):
    # 获取部分数据
    def get(request):
        # 先从缓存中读取数据
        res = cache.get('res')
        if res is None:
            res = {}
            case = {}
            host = {}
            nodes = {}
            device = {}
            software = {}
            weapon = {}
            template = {}
            case_top = {}
            machine_top = {}
            sql_one = """ SELECT count(*) AS value,s.discription as name FROM b_case as b join sys_code_dict as s where s.code_id=b.state GROUP BY state; """
            sql_two = """ SELECT count(*) AS value,s.discription as name FROM b_case as b join sys_code_dict as s WHERE b.field_oriented=s.code_id GROUP BY field_oriented; """
            sql_three = """ select COUNT(*) as value,node_os as name
                    from b_case a
                    left join b_topological_structure b on a.case_id = b.case_id
                    left join  b_node c on  c.node_id = (select node_id from b_node where node_type = 'h' and b.topological_id = topological_id limit 1)
                    left join b_node_interface d on c.node_id = d.node_id
                    left join auth_user e on a.creator_id = e.id
                    left join sys_code_dict f on a.state = f.code_id
                    where  a.field_oriented=201011
                    GROUP BY node_os"""
            sql_four = """select COUNT(*) as value,f.discription as name
                    from b_case a
                    join sys_code_dict f on a.state = f.code_id
                    where  a.field_oriented=201011
                    GROUP BY a.state;
            """
            sql_five = """SELECT count(*) AS value,node_type as name FROM b_node WHERE node_type is not NULL GROUP BY node_type;"""
            sql_six = """SELECT count(*) AS value,node_category as name FROM b_node WHERE node_type is not NULL GROUP BY node_category;"""
            sql_seven = """SELECT COUNT(*) as value,s.code_name as name FROM b_machine as b join sys_code_dict as s where b.machine_type=s.code_id  GROUP BY machine_type;"""
            sql_eight = """SELECT COUNT(*) as value,s.code_name as name FROM b_software as b join sys_code_dict as s WHERE b.software_type=s.code_id and b.classify=1 GROUP BY b.software_type;"""
            sql_nine = """SELECT COUNT(*) as value,s.code_name as name FROM b_software as b join sys_code_dict as s WHERE b.software_type=s.code_id and b.classify=2 GROUP BY b.software_type;"""
            sql_ten = """SELECT COUNT(*) as value,system as name FROM b_software  WHERE classify=1 GROUP BY system;"""
            sql_ten1 = """SELECT COUNT(*) as value,system as name FROM b_software  WHERE classify=2 GROUP BY system;"""
            sql_temp = """SELECT COUNT(*) as value,os_type as name FROM b_vm_template GROUP BY os_type;"""
            sql_case_top = """SELECT
                            count(a.node_id) AS value,
                            c.name AS name
                        FROM
                            b_node a
                        LEFT JOIN b_topological_structure b ON a.topological_id = b.topological_id
                        INNER JOIN b_case c on c.case_id=b.case_id
                        GROUP BY
                            b.case_id

                        ORDER BY value desc
                        LIMIT 10
                        """
            sql_machine_top = """SELECT
                            COUNT(*) AS
                        value
                            ,
                            machine_name AS name
                        FROM
                            b_node AS b
                        JOIN b_machine AS m
                        WHERE
                            b.machine_id = m.machine_id
                        AND machine_name IS NOT NULL
                        GROUP BY
                            machine_name
                        ORDER BY

                        value
                            DESC
                        LIMIT 10"""
            try:
                # 实例管理
                with connection.cursor() as cursor:
                    cursor.execute(sql_one)
                    result = dictfetchall(cursor)
                    case['in'] = result

                with connection.cursor() as cursor:
                    cursor.execute(sql_two)
                    result = dictfetchall(cursor)
                    case['out'] = result

                res['case'] = case
                # 主机股哪里
                with connection.cursor() as cursor:
                    cursor.execute(sql_three)
                    result = dictfetchall(cursor)
                    host['in'] = result

                with connection.cursor() as cursor:
                    cursor.execute(sql_four)
                    result = dictfetchall(cursor)


                    host['out'] = result

                res['host'] = host
                # 节点管理
                with connection.cursor() as cursor:
                    cursor.execute(sql_five)
                    result = dictfetchall(cursor)
                    nodes['out'] = result

                with connection.cursor() as cursor:
                    cursor.execute(sql_six)
                    result = dictfetchall(cursor)

                    result[0]['name'] = "仿真"
                    result[1]['name'] = "数模"

                    result[2]['name'] = "实物"
                    result[3]['name'] = "模拟"
                    nodes['in'] = result
                res['nodes'] = nodes
                # 设备管理
                with connection.cursor() as cursor:
                    cursor.execute(sql_seven)
                    result = dictfetchall(cursor)
                    device['in'] = result
                res['device'] = device
                # 软件管理
                with connection.cursor() as cursor:
                    cursor.execute(sql_eight)
                    result = dictfetchall(cursor)
                    software['out'] = result

                with connection.cursor() as cursor:
                    cursor.execute(sql_ten)
                    result = dictfetchall(cursor)
                    software['in'] = result

                res['software'] = software
                # 武器管理
                with connection.cursor() as cursor:
                    cursor.execute(sql_nine)
                    result = dictfetchall(cursor)
                    weapon['out'] = result

                with connection.cursor() as cursor:
                    cursor.execute(sql_ten1)
                    result = dictfetchall(cursor)
                    weapon['in'] = result

                res['weapon'] = weapon

                # 模板管理
                with connection.cursor() as cursor:
                    cursor.execute(sql_temp)
                    result = dictfetchall(cursor)
                    template['in'] = result

                res['template'] = template
                # 统计实例包含的节点数top10
                with connection.cursor() as cursor:
                    cursor.execute(sql_case_top)
                    result = dictfetchall(cursor)
                    case_top['in'] = result

                res['case_top'] = case_top
                # 统计设备上节点数前10位的设备
                with connection.cursor() as cursor:
                    cursor.execute(sql_machine_top)
                    result = dictfetchall(cursor)
                    machine_top['in'] = result

                res['machine_top'] = machine_top
                # 数据不存在，则进行查询，把数据放入缓存中
                cache.set('res', res, 3600)

            except Exception as e:
                pass
        else:
            res = res
        return JsonResponse(res)


def large(request):
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    view={}
    s = datetime.datetime.now()
    n=request.REQUEST.get('n',24)
    # filename = json.loads(request.REQUEST['filename'])
    filename=request.REQUEST.get('filename',s.strftime('%Y%m%d%H%M%S') + str(s).split('.')[1])

    field_oriented = request.REQUEST.get('category', "201001")
    code = request.REQUEST['code']
    # view = json.loads(request.REQUEST['view'])
    # view['name'], view['descr'], view['option']['delay'], view['option']['datarate'], view['option']['mtu']
    view['name']=' Ftps协议分析11'
    view['descr'] = '星型'
    view['delay'] = 2
    view['datarate'] = 56
    view['mtu'] = 1400
    person_id = request.session.get("login_id", 0)
    sql_one = """
            insert into b_topic_task(name, type, caseId, state, send_time)
            values('TOPOLOGY', 'T', '%s', '0', now())
        """


    case_id = request.REQUEST.get('id', s.strftime('%Y%m%d%H%M%S') + str(s).split('.')[1])

    result = {'flag': False}
    db = database.DB()
    db.connect()
    task_id = db.execute_sql(sql_one % case_id)
    db.close()
    # # 开启节点位置信息生成线程
    # ts = threading.Thread(target=get_data_topo, args=(n))
    # # 开启节点的xml等信息的生成
    # t = threading.Thread(target=build_large,
    #                      args=(task_id, filename, field_oriented, code, view, case_id, person_id))
    # ts.start()
    # t.start()
    result['flag'] = True
    result['task_id'] = task_id
    return HttpResponse(json.dumps(result, default=utils.json_encoder))



def build_suplarge(task_id=None, filename=None, field_oriented=None, code=None, view=None, case_id=None, person_id=None):
    # reload(sys)
    # sys.setdefaultencoding('utf-8')

    db = database.DB()
    db.connect()
    result = {'flag': False}
    start = time.time()
    # logger.debug('#'*10)
    # return HttpResponse(json.dumps(result, default=utils.json_encoder))
    case_path = os.path.join(settings.NFS_ROOT, 'CaseDefinitions')
    sql_one = """
        update b_topic_task set recv_msg = '%s', recv_time = now(), state = '%s', duration = %s
        where taskid = %s
    """
    begin = datetime.datetime.now()
    if not os.path.exists(case_path):
        info = "nfs not mount"
        result['info'] = info
        db.execute_sql(sql_one % (info, '1', 0, task_id))
        db.close()
        return result

    a_dir = os.path.join(case_path, str(case_id), case_dir['a'])
    m_dir = os.path.join(case_path, str(case_id), case_dir['m'])
    p_dir = os.path.join(case_path, str(case_id), case_dir['p'])
    t_dir = os.path.join(case_path, str(case_id), case_dir['t'])

    if not os.path.exists(a_dir):
        os.makedirs(a_dir)
    if not os.path.exists(m_dir):
        os.makedirs(m_dir)
    if not os.path.exists(p_dir):
        os.makedirs(p_dir)
    if not os.path.exists(t_dir):
        os.makedirs(t_dir)

    os.chmod(m_dir, stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)

    sql = """
        select topological_id from b_topological_structure where case_id = '%s'
    """ % (case_id)

    # delete b_topological_structure  b_topological_relation b_node b_node_interface a_node_conf_rules a_port_filter
    # logger.debug('one must %s seconds' % (time.time()-start))
    topological_id = db.query_sql(sql)
    if len(topological_id) > 0:
        sql = """
            delete from b_topological_structure
            where case_id = '%s'
        """ % (case_id)
        db.execute_sql(sql)
        # topological_node = []
        for value in topological_id:
            sql = """
                delete from b_node_interface where node_id in (select node_id from b_node where  topological_id = %s)
            """ % (value['topological_id'])
            db.execute_sql(sql)
            sql = """
                delete from a_port_filter where node_id in (select node_id from b_node where  topological_id = %s)
            """ % (value['topological_id'])
            db.execute_sql(sql)
            sql = """
                delete from a_node_conf_rules where node_id in (select node_id from b_node where  topological_id = %s)
            """ % (value['topological_id'])
            db.execute_sql(sql)
            sql = """
                delete from b_node where topological_id = %s
            """ % (value['topological_id'])
            db.execute_sql(sql)
            sql = """
                delete from b_topological_relation where topological_id = %s
            """ % (value['topological_id'])
            db.execute_sql(sql)
            # topological_node.append(node_id)
    else:
        pass

    # 插入新数据至b_topological_structure
    sql = """
        INSERT INTO b_topological_structure
        (
          topological_name,topological_discription,draw_type,delay,datarate,mtu,create_time,person_id,status,case_id
        )
        VALUE
        (
          '%s','%s','draw',%s,%s,%s,now(),%s,'1','%s'
        )
    """ % (view['name'], view['descr'], view['delay'], view['datarate'], view['mtu'], person_id, case_id)

    topological_id = db.execute_sql(sql)

    # 获取节点的ownership_type
    ownership_type = "202001"
    sql = """
        select code_id from sys_code_dict where dict_id = "NEUTRAL"
    """
    res = db.query_sql(sql)
    for i in res:
        if i['code_id'] is not None:
            ownership_type = i['code_id']

    # 插入新数据至b_node
    sql = """
        select * from a_all_conf_rules
    """
    res = db.query_sql(sql)

    conf_rules = {}
    for v in res:
        if not conf_rules.get(v['using_type'], False):
            conf_rules[v['using_type']] = []
        conf_rules[v['using_type']].append(v)

    # file = os.path.join(settings.BASE_DIR, 'media', 'share', 'CaseDefinitions', 'configTopo', (str(filename) + '.xml'))
    file = os.path.join(settings.BASE_DIR, 'media', 'share', 'ConfigTopo', (str(filename) + '.xml'))
    if not os.path.exists(file):
        info = '{0}.xml is not exist'.format(filename)
        result['info'] = info
        db.execute_sql(sql_one % (info, '1', 0, task_id))
        db.close()
        return result
    view['min'] = 0
    view['max'] = 0
    # logger.debug('one_one must %s seconds' % (time.time()-start))
    tree = ET.parse(file)
    root = tree.getroot()
    node_map = {}
    node_dict = {}
    links_dict = {}
    order = 0

    # logger.debug('begin')
    for tag in root:
        order += 1
        # logger.debug(order)
        tag_ = tag.tag
        if tag_ == 'link_information' or tag_ == 'id_range':
            continue
        else:
            id_ = tag.attrib['id']
            links = tag.findall('interface')
            links_dict[id_] = links
            nic_number = len(links)
            node = {}
            node['node_name'] = tag_ + '_' + str(order)
            tag_0 = tag_.split('_')[0]
            node['node_category'] = tag_0 if tag_0 != tag_ else 'sim'
            node['node_type'] = node_types_[tag_.split('_')[1] if tag_0 != tag_ else tag_]
            node['nic_number'] = nic_number
            node['topological_id'] = topological_id
            node['ownership_type'] = '202001'
            node['hypervisor'] = 'xen'
            node['memory'] = 512
            node['cpu_number'] = 1
            node['node_os'] = 'windows'
            node['arch'] = '32位'
            node['machine'] = 'hvm'
            node['vm_template_id'] = 0

            params = (node['node_name'], node['node_category'], node['node_type'], node['nic_number'], node['topological_id'], node['ownership_type'],
                      node['hypervisor'], node['memory'], node['cpu_number'], node['node_os'], node['arch'], node['machine'], node['vm_template_id'])
            sql = """
                insert into b_node
                (
                  base_node_id, node_name, node_category,node_type,nic_number,create_time,topological_id,ownership_type, hypervisor, memory, cpu_number, node_os, arch, machine, vm_template_id
                )
                values
                (
                  0,'%s','%s', '%s', %s, now(), %s, '%s', '%s', %s, %s, '%s', '%s', '%s', %s
                )
            """
            node['id'] = db.execute_sql(sql % params)
            # logger.debug('ok')
            node_dict[str(node['id'])] = node
            if view['min'] == 0:
                view['min'] = node['id']
            view['max'] = node['id']
            node_map[id_] = node['id']

    sql_list = []
    prefix = """
        INSERT INTO b_node_interface(interface_id, node_id, link_node_id, nic_ip_address, nic_subnet_mask, gateway)
        VALUES
    """
    for id_, links in links_dict.items():
        for link in links:
            interface_id = link.attrib['id']
            node_id = node_map[id_]
            link_node_id = node_map[link.find('link').text]
            nic_ip_address = 'default'
            nic_subnet_mask = 'default'
            gateway = 'default'

            # sql = """
            #     insert into b_node_interface
            #     (
            #         interface_id,node_id,link_node_id, nic_ip_address,nic_subnet_mask,gateway,create_time
            #     )
            #     values
            #     (
            #         %s, %s, %s, '%s', '%s', '%s', now()
            #     )
            # """ % (interface_id, node_id, link_node_id, nic_ip_address, nic_subnet_mask, gateway)
            # db.execute_sql(sql)
            params = (interface_id, node_id, link_node_id, nic_ip_address, nic_subnet_mask, gateway)
            prefix += str(params) + ',' + '\n\t'

    sql_two = prefix.rsplit(',', 1)[0]
    # logger.debug(sql_one)
    db.execute_sql(sql_two)
    # logger.debug('oooooooo')
    # db.execute_sql(sql_one)
    # logger.debug('one_two must %s seconds' % (time.time()-start))
    # 获取case的定义状态
    sql = """
        select code_id from sys_code_dict where dict_id = "DEFINED"
    """
    res = db.query_sql(sql)
    define_code_id = "200501"
    for i in res:
        if i['code_id'] is not None:
            define_code_id = i['code_id']

    # 获取field_oriented值
    # sql = """
    #     select code_id from sys_code_dict where dict_id = "FIELD_SINGLE"
    # """
    # res = db.query_sql(sql)
    # for i in res:
    #     if i['code_id'] is not None:
    #         field_oriented = i['code_id']

    case_path_base = 'CaseDefinitions'
    a_file_base = os.path.join(case_path_base, str(case_id), case_dir['a'], 'a' + str(topological_id) + '.xml')
    m_file_base = os.path.join(case_path_base, str(case_id), case_dir['m'], 'm' + str(topological_id) + '.xml')
    p_file_base = os.path.join(case_path_base, str(case_id), case_dir['p'], 'p' + str(topological_id) + '.xml')
    t_file_base = os.path.join(case_path_base, str(case_id), case_dir['t'], 't' + str(topological_id) + '.xml')

    sql = """
        select * from b_case where case_id='%s'
    """ % case_id
    res = db.query_sql(sql)
    # logger.debug(topological_id)
    # logger.debug(t_file_base)
    # logger.debug(case_id)
    if len(res) > 0:
        # logger.debug(t_file_base)
        # 更新数据至b_case
        sql = """
            update b_case set name='%s', description='%s', updator_id=%s, update_time=now(), state='%s',tfile='%s'
            where case_id='%s'
        """ % (view['name'], view['descr'], person_id, define_code_id, t_file_base, case_id)
        # logger.debug(sql)
        rrrr = db.update_sql(sql)
        # logger.debug(rrrr)
    else:
        # 插入新数据至b_case
        sql = """
            insert into b_case(case_id, base_case_id, is_template, name, tfile, afile, mfile, pfile, state, field_oriented,creator_id, create_time, updator_id, update_time, description)
            values('%s', '%s', '1', '%s', '%s', '%s', '%s', '%s','%s', '%s', %s, now(), %s, now(), '%s')
        """ % (case_id, '0', view['name'], t_file_base, a_file_base, m_file_base, p_file_base, define_code_id, field_oriented, person_id, person_id, view['descr'])
        db.execute_sql(sql)

    # logger.debug('two must %s seconds' % (time.time()-start))
    topological_file = 't' + str(topological_id) + '.xml'
    shutil.copy2(file, os.path.join(t_dir, topological_file))
    tree2 = ET.parse(os.path.join(t_dir, topological_file))
    root2 = tree2.getroot()
    for tag in root2:
        if tag.tag == 'id_range':
            tag.set('min', str(view['min']))
            tag.set('max', str(view['max']))
            continue
        if tag.tag == 'link_information':
            continue
        tag.set('id', str(node_map[str(tag.attrib['id'])]))
        # tag.attrib['id'] = node_map[str(tag.attrib['id'])]
        links = tag.findall('interface')
        for link in links:
            link.find('link').text = str(node_map[str(link.find('link').text)])

    tree2.write(os.path.join(t_dir, topological_file), encoding='utf-8', xml_declaration=True)
    # logger.debug('three must %s seconds' % (time.time()-start))


    t_file = 't' + str(case_id) + '.xml'
    build_t_xml_(os.path.join(case_path, str(case_id), t_file), root, node_dict, node_map)
    # logger.debug('four must %s seconds' % (time.time()-start))

    h_file = 'h' + str(case_id) + '.xml'
    build_h_xml(os.path.join(case_path, str(case_id), h_file), code)
    # logger.debug('five must %s seconds' % (time.time()-start))

    v_file = 'v' + str(case_id) + '.xml'
    build_v_xml(os.path.join(case_path, str(case_id), v_file), view, [], [])
    # logger.debug('six must %s seconds' % (time.time()-start))

    sql = """
        INSERT INTO
        b_topological_relation
        (
          topological_id,back_xml_name,view_xml_name,list_xml_name
        )
        VALUE
        (
          %s,'%s','%s','%s'
        )
    """ % (topological_id, t_file, v_file, h_file)
    db.execute_sql(sql)

    result['flag'] = True
    result['id'] = case_id
    end = datetime.datetime.now()
    second = (end - begin).seconds
    db.execute_sql(sql_one % ('', '2', second, task_id))
    db.close()
    # logger.debug('seven must %s seconds' % (time.time()-start))

    return result


def build_suplarge_top(request):

    pass
