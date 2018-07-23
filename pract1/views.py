from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django.db import connection
from django.core.cache import cache
import time

# Create your views here.
class Meyhod(View):
    def get(self,request):
        n = 500
        # 初始坐标
        pos = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        r = 4
        d = 1
        count = 0
        res = {}
        node_id = 1
        top_json = {}

        middle_point = [0, 0, 0]
        firewall = []
        ips = []
        ids = []
        router = []
        server = []


        top_json['firewall'] = firewall
        top_json['ips'] = ips
        top_json['ids'] = ids
        top_json['middle_point']=middle_point
        top_json['router'] = router
        top_json['server'] = server
        nodes_list1 = []
        nodes_list2 = []
        index = [1, 5, n*4-3, n*4+1]
        for k in range(1, 18):
            y = r * k
            if k == 1:
                for i in range(1, n):
                    for j in range(1, n):
                        for s in range(len(pos)):
                            nodes_list2.append([i * pos[s][0], y, j * pos[s][1]])
                            nodes_list1.append([str(node_id), 'host', i * pos[s][0], y, j * pos[s][1], 0.9])
                            # nodes_list1.append([node_id + 1, 'host', i * pos[s][0], y, -j * pos[s][1], 0.9])
                            # nodes_list1.append([node_id + 2, 'host', -i * pos[s][0], y, j * pos[s][1], 0.9])
                            # nodes_list1.append([node_id + 3, 'host', -i * pos[s][0], y, -j * pos[s][1], 0.9])
                            count += 1
                            node_id += 1
                            top_json['host'] = nodes_list1

            else:

                yb = r * (k - 1)
                for i in range(1, n):
                    for j in range(1, n):
                        for s in range(len(pos)):
                            nodes_list2.append([pos[s][0] * (d * (i - 0.5) + 0.5), y,
                                           (d * (j - 0.5) + 0.5) * pos[s][1]])
                            nodes_list1.append(
                                [str(node_id),
                                 'switch',
                                 pos[s][0] * (d * (i - 0.5) + 0.5),
                                 y,

                                (d * (j - 0.5) + 0.5) * pos[s][1],
                                 0.9,
                                 "lvmy",
                                 3802,
                                 [],

                                 [str(index[0]), str(index[1]), str(index[2]), str(index[3])]])
                            # index=[str(index[0]+1),str(index[1]+1),str(index[2]+1),str(index[3]+1)]
                            if index[0] % 4 == 0:
                                index = [index[0] + 5, index[0] + 9, index[2] + 5, index[2] + 9]
                            else:
                                index = [index[0] + 1, index[0] + 5, index[2] + 1, index[3] + 1]
#                             x=[str(nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5)-0.5, y-4,(d * (j - 0.5) + 0.5) * pos[s][1]-0.5])+1),
# str(nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5)-0.5, y-4,(d * (j - 0.5) + 0.5) * pos[s][1]+0.5])+1),
# str(nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5)+0.5, y-4,(d * (j - 0.5) + 0.5) * pos[s][1]-0.5])+1),
# str(nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5)+0.5, y-4,(d * (j - 0.5) + 0.5) * pos[s][1]+0.5])+1)]
#                             print(x)
                            count += 1
                            node_id += 1
                            top_json['host'] = nodes_list1

            n = int(n * 0.5)
            d = d * 2
        res['top_json']=top_json
        res['number']=count
        print(count)
        return JsonResponse(res)


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
# class Ms(View):
#     def get(self):
#
#         res={'flag':False}
#         # return HttpResponse(res)

def get_case_data(request):
    # 先从缓存中读取数据
    res=cache.get('res')
    if res is None:
        res={}
        case = {}
        host={}
        nodes={}
        device={}
        software={}
        weapon={}
        template={}
        case_top={}
        machine_top={}
        sql_one = """SELECT count(*) AS value,s.discription as name FROM b_case as b join sys_code_dict as s where s.code_id=b.state GROUP BY state;"""
        sql_two = """SELECT count(*) AS value,s.discription as name FROM b_case as b join sys_code_dict as s WHERE b.field_oriented=s.code_id GROUP BY field_oriented;"""
        sql_three="""select COUNT(*) as value,node_os as name
                from b_case a
                left join b_topological_structure b on a.case_id = b.case_id
                left join  b_node c on  c.node_id = (select node_id from b_node where node_type = 'h' and b.topological_id = topological_id limit 1)
                left join b_node_interface d on c.node_id = d.node_id
                left join auth_user e on a.creator_id = e.id
                left join sys_code_dict f on a.state = f.code_id
                where  a.field_oriented=201011
                GROUP BY node_os"""
        sql_four="""select COUNT(*) as value,f.discription as name
                from b_case a
                join sys_code_dict f on a.state = f.code_id
                where  a.field_oriented=201011
                GROUP BY a.state;
        """
        sql_five ="""SELECT count(*) AS value,node_type as name FROM b_node WHERE node_type is not NULL GROUP BY node_type;"""
        sql_six="""SELECT count(*) AS value,node_category as name FROM b_node WHERE node_type is not NULL GROUP BY node_category;"""
        sql_seven="""SELECT COUNT(*) as value,s.code_name as name FROM b_machine as b join sys_code_dict as s where b.machine_type=s.code_id  GROUP BY machine_type;"""
        sql_eight="""SELECT COUNT(*) as value,s.code_name as name FROM b_software as b join sys_code_dict as s WHERE b.software_type=s.code_id and b.classify=1 GROUP BY b.software_type;"""
        sql_nine = """SELECT COUNT(*) as value,s.code_name as name FROM b_software as b join sys_code_dict as s WHERE b.software_type=s.code_id and b.classify=2 GROUP BY b.software_type;"""
        sql_ten="""SELECT COUNT(*) as value,system as name FROM b_software  WHERE classify=1 GROUP BY system;"""
        sql_ten1 = """SELECT COUNT(*) as value,system as name FROM b_software  WHERE classify=2 GROUP BY system;"""
        sql_temp="""SELECT COUNT(*) as value,os_type as name FROM b_vm_template GROUP BY os_type;"""
        sql_case_top="""SELECT
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
        sql_machine_top="""SELECT
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
                case['in']=result

            with connection.cursor() as cursor:
                cursor.execute(sql_two)
                result = dictfetchall(cursor)
                case['out'] = result

            res['case']=case
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
                nodes['in'] = result
            res['nodes']=nodes
            # 设备管理
            with connection.cursor() as cursor:
                cursor.execute(sql_seven)
                result = dictfetchall(cursor)
                device['in'] = result
            res['device']=device
            #软件管理
            with connection.cursor() as cursor:
                cursor.execute(sql_eight)
                result = dictfetchall(cursor)
                software['out'] = result

            with connection.cursor() as cursor:
                cursor.execute(sql_ten)
                result = dictfetchall(cursor)
                software['in'] = result

            res['software']=software
            #武器管理
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

            res['case_top']=case_top
            # 统计设备上节点数前10位的设备
            with connection.cursor() as cursor:
                cursor.execute(sql_machine_top)
                result = dictfetchall(cursor)
                machine_top['in'] = result

            res['machine_top'] = machine_top
            # 数据不存在，则进行查询，把数据放入缓存中
            cache.set('res',res,30)

        except Exception as e:
            pass
    else:
        res=res
    return JsonResponse(res)