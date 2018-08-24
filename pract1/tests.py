from django.test import TestCase
import datetime
# Create your tests here.
def get_suptop_data(request):
    res = {}
    db = database.DB()
    db.connect()
    # 1.获取前端传来的tasks_id
    tasks_id=request.REQUEST.get('tasks_id')
    # 2.数据库查询节点信息
    # 获取任务表中的实例id
    sql="""SELECT caseId from b_topic_task WHERE taskid=%s"""
    caseId = db.query_sql(sql % tasks_id)
    # topological_id
    sql="""SELECT topological_id from b_topological_structure WHERE case_id=%s"""
    topological_id = db.query_sql(sql % caseId)
    #获取节点的相关信息
    sql="""SELECT node_id,node_type from b_node WHERE topological_id=%s"""
    topo_node_info = db.query_sql(sql % topological_id)

    # 3.读取json文件获取节点位置信息
    case_path = os.path.join(settings.NFS_ROOT, 'CaseDefinitions', '20160802145159627416')
    with open(case_path + '/topology.json', 'rb') as f:
        data = json.load(f)
        count = len(data)

    # 4.组织数据返回前端页面

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
    top_json['middle_point'] = middle_point
    top_json['router'] = router
    top_json['server'] = server
    top_json['count'] = count
    res['top_json'] = top_json
    res['top_node'] = data

    res['top_node_info'] = topo_node_info

    return JsonResponse(res)
